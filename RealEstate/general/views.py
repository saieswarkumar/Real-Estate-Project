from django.shortcuts import render, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import Profile
from .forms import SignUpForm

@login_required(login_url='/login/')
def home(request):
    if request.user.user_type == 'AG':
        return redirect('agents:home')
    elif request.user.user_type == 'BU':
        return redirect('buyers:home')
    elif request.user.user_type == 'SE':
        return redirect('sellers:home')
    else:
        return redirect('generals:logout')

"""
def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            #user.refresh_from_db()  # load the profile instance created by the signal
            #user.profile.user_type = form.cleaned_data.get('usertype')
            #user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            if user.is_active:
                login(request, user)
            return redirect('/login/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
"""

def login_user(request, template_name):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('generals:home')
    return render(request,template_name, )

def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.save()
            return redirect('/login/')
    else:
        form = SignUpForm()
    return render(request, 'general/signup.html', {'form': form})

def signupag(request):
    if request.method == 'POST':
        form = SignUpFormag(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpFormag()
    return render(request, 'general/signup.html', {'form': form})