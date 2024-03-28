from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PropertyRequests
from general.models import Profile

class PropertyRequestsForm(forms.ModelForm):
    message=forms.CharField(label='search', widget=forms.TextInput(attrs={'placeholder': 'Search'}))
    class Meta:
        model = PropertyRequests
        fields = ('status','price','message',)