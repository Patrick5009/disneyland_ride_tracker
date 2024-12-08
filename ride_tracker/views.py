from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def index(request):
    ride_tracker = Ride.objects.all()

    form = RideForm()

    if request.method == 'POST':
        form = RideForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

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
    return render(request, 'ride_tracker/delete.html') 
