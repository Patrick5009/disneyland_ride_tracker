from django.shortcuts import render, redirect, get_object_or_404  
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required  
from .models import *  
from .forms import *  


# Main page to display the ride tracker

@login_required
def index(request):
    # filter for the specific user
    ride_tracker = Ride.objects.filter(user=request.user)
    form = RideForm()  

    # get the ride name from the form
    if request.method == 'POST':
        ride_name = request.POST.get('ride_name')  
        state = request.POST.get('state') == 'on'  

        # only save it if a ride name is given
        if ride_name:  
            Ride.objects.create(
                ride_name=ride_name,
                state=state,
                user=request.user  
            )
            # success message
            messages.success(request, f'Ride "{ride_name}" has been added to the tracker!')
        return redirect('/')  

    context = {'ride_tracker': ride_tracker, 'form': form}
    return render(request, 'ride_tracker/rides.html', context)




# Update the ride list

@login_required
def updateRide(request, pk):
    # make sure ride belongs to the logged in user
    ride = get_object_or_404(Ride, id=pk, user=request.user)
    form = RideForm(instance=ride)

    # update data and save
    if request.method == 'POST':
        form = RideForm(request.POST, instance=ride)
        if form.is_valid():
            form.save()
            messages.success(request, f'Ride "{ride.ride_name}" has been updated successfully!')
            return redirect('/')

    context = {'form': form}
    return render(request, 'ride_tracker/update_ride.html', context)




# Deleting rides

@login_required
def deleteRide(request, pk):
    # make sure the ride belongs to the logged in user
    item = get_object_or_404(Ride, id=pk, user=request.user)

    if request.method == 'POST':
        # delete the ride 
        item.delete()
        messages.success(request, f'Ride "{item.ride_name}" has been deleted from the tracker.')
        return redirect('/')

    context = {'item': item}
    return render(request, 'ride_tracker/delete.html', context)
