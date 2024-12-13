from django import forms
from django.forms import ModelForm

from .models import *

# Form for the Ride model


class RideForm(forms.ModelForm):

    class Meta:
        model = Ride

        # Specify fields to include in the form
        fields = ['ride_name', 'state']

        # Provide a custom label for the 'state' field
        labels = {'state': 'Visited this ride?', }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add predefined rides for the dropdown and placeholder text
        self.fields['ride_name'].widget = forms.TextInput(attrs={
            'list': 'rides-list',
            'placeholder': 'Select or type a ride name'
        })
