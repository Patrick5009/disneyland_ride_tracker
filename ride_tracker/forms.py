from django import forms
from django.forms import ModelForm

from .models import *


class RideForm(forms.ModelForm):
    
    class Meta:
        model = Ride
        fields = ['ride_name', 'state']
        labels = {'state': 'Visited this ride?',}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add predefined rides for the dropdown
        self.fields['ride_name'].widget = forms.TextInput(attrs={
            'list': 'rides-list',
            'placeholder': 'Select or type a ride name'
        })