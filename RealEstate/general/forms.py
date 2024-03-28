from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets
from .models import Profile
from .choices import *

class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'name'})),
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password'})),
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password'})),
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password'})),
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'firstname'})),
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'lastname'})),
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'email'})),
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'location'})),
    user_type = forms.ChoiceField(choices=type_choices, widget=forms.Select(attrs={'class': 'selectstyle'}), required=True)
    

    class Meta:
        model = Profile
        widgets = {
            'username' : forms.TextInput(attrs = {'placeholder': 'Username','class': 'name'}),
            'password' : forms.PasswordInput(attrs = {'placeholder': 'Password','class': 'password'}),
            'password1' : forms.PasswordInput(attrs = {'placeholder': 'Password','class': 'password'}),
            'password2' : forms.PasswordInput(attrs = {'placeholder': 'Password','class': 'password'}),
            'first_name' : forms.TextInput(attrs = {'placeholder': 'First Name','class': 'firstname'}),
            'last_name' : forms.TextInput(attrs = {'placeholder': 'Last Name','class': 'lastname'}),
            'email'    : forms.EmailInput(attrs = {'placeholder': 'E-Mail','class': 'email'}),
            'location'    : forms.TextInput(attrs = {'placeholder': 'Location','class': 'location'}),
            'user_type'    : forms.TextInput(attrs = {'class': 'selectstyle'}),
        }
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'location', 'user_type' )

class SignUpFormag(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        widgets = {
            'username' : forms.TextInput(attrs = {'placeholder': 'Username','class': 'name'}),
            'password1' : forms.PasswordInput(attrs = {'placeholder': 'Password','class': 'password'}),
            'password2' : forms.PasswordInput(attrs = {'placeholder': 'Password','class': 'password'}),
            'first_name' : forms.TextInput(attrs = {'placeholder': 'First Name','class': 'firstname'}),
            'last_name' : forms.TextInput(attrs = {'placeholder': 'Last Name','class': 'lastname'}),
            'email'    : forms.EmailInput(attrs = {'placeholder': 'E-Mail','class': 'email'}),
            'location'    : forms.TextInput(attrs = {'placeholder': 'Location','class': 'location'}),
            'user_type'    : forms.TextInput(attrs = {'class': 'selectstyle'}),
        }
        fields = ('username', 'birth_date', 'email', )