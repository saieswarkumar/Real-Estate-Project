from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import PropertyDetails, LocationDetails

class GetPropertyDetailsForm(forms.ModelForm):
    class Meta:
        model = PropertyDetails
        fields = ('city', 'address', 'ploatarea', 'bedrooms', 'bathrooms', 'balconies', 'totalrooms', 'totalfloors','houseimage','houseimage2','houseimage3', 'neighbour', 'aboutprop',)

class GetLocationForm(forms.ModelForm):
    class Meta:
        model = LocationDetails
        fields = ('locaddress',)

class LocationMapForm(forms.ModelForm):
    class Meta:
        model = LocationDetails
        fields = ('locaddress', 'locationusage', 'otherdetails',)