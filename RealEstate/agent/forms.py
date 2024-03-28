from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Chat
from general.models import Profile

class ChatForm(forms.ModelForm):
    message=forms.CharField(widget=forms.TextInput({'placeholder': 'Type Your Message Here ..'}))
    class Meta:
        model = Chat
        fields = ('message',)