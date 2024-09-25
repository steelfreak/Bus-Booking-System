# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from .forms import CustomUserCreationForm
from .forms import ProfileForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            phone_number = form.cleaned_data.get('phone_number')
            Profile.objects.create(user=user, phone_number=phone_number, email=user.email)
            messages.success(request, 'Registration successful.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a home page or other protected page
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html')



def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout




@login_required
def home(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'accounts/home.html', {'profile': profile})



@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('home')  # Redirect to a relevant page after saving
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/edit_profile.html', {'form': form})
