from django import forms
from django.forms import ModelForm

from .models import *


class RideForm(forms.ModelForm):
    
    class Meta:
        model = Ride
        fields = ['ride_name', 'state']
        labels = {'state': 'Visited this ride?',}