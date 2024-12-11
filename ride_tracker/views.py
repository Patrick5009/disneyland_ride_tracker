from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.

def index(request):
    ride_tracker = Ride.objects.all()
    form = RideForm()  # Single instance of the form

    if request.method == 'POST':
        ride_name = request.POST.get('ride_name')  # Get the ride name from the form
        state = request.POST.get('state') == 'on'  # Convert checkbox to boolean

        if ride_name:  # Only save if a ride name is provided
            Ride.objects.create(
                ride_name=ride_name,
                state=state,
                user=request.user if request.user.is_authenticated else None
            )
            # Add a success message
            messages.success(request, f'Ride "{ride_name}" has been added to the tracker!')
        return redirect('/')  # Redirect to the same page after handling POST

    context = {'ride_tracker': ride_tracker, 'form': form}
    return render(request, 'ride_tracker/rides.html', context)


def updateRide(request, pk):
    # Fetch the ride instance to update based on the primary key (pk)
    ride = Ride.objects.get(id=pk)

    # Create a form instance pre-filled with the data from the ride instance
    form = RideForm(instance=ride)

    if request.method == 'POST':
        # If the form is submitted, populate it with the updated data from the POST request
        form = RideForm(request.POST, instance=ride)
        if form.is_valid():
            # If the form data is valid, save the updated ride to the database
            form.save()
            # Add a success message
            messages.success(request, f'Ride "{ride.ride_name}" has been updated successfully!')
            # Redirect to the homepage after successful update
            return redirect('/')

    # Render the update form template with the pre-filled form
    context = {'form': form}
    return render(request, 'ride_tracker/update_ride.html', context)


def deleteRide(request, pk):
    # Fetch the ride instance to delete based on the primary key (pk)
    item = Ride.objects.get(id=pk)

    if request.method == 'POST':
        # If the form is submitted, delete the ride from the database
        item.delete()
        # Add a success message
        messages.success(request, f'Ride "{item.ride_name}" has been deleted from the tracker.')
        # Redirect to the homepage after successful deletion
        return redirect('/')

    # Render the delete confirmation template
    context = {'item': item}
    return render(request, 'ride_tracker/delete.html', context)
