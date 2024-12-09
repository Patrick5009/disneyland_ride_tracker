from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def index(request):
    ride_tracker = Ride.objects.all()

    form = RideForm()

    if request.method == 'POST':
        ride_name = request.POST.get('ride_name')  # Get the ride name from the form
        state = request.POST.get('state') == 'on'  # Convert checkbox to boolean

        if ride_name:  # Only save if a ride name is provided
            Ride.objects.create(ride_name=ride_name, state=state, user=request.user if request.user.is_authenticated else None)
        return redirect('/')
        # old code below/ get rid before due time
        # form = RideForm(request.POST)
        # if form.is_valid():
        #     form.save()
        # return redirect('/')
    form = RideForm()
    context = {'ride_tracker':ride_tracker, 'form':form}
    return render(request, 'ride_tracker/rides.html', context)


def updateRide(request, pk):
    ride = Ride.objects.get(id=pk)

    form = RideForm(instance=ride)

    if request.method == 'POST':
        form = RideForm(request.POST, instance=ride)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request, 'ride_tracker/update_ride.html', context)


def deleteRide(request, pk):
    item = Ride.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'ride_tracker/delete.html', context) 
