from django.shortcuts import render, redirect
from head.models import Profile
from .forms import *
from django.contrib.auth import login, logout

def sign_up(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
       user = form.save()
       Profile.objects.create(user=user)
       return redirect('head:home')
    return render(request, 'sign_up.html', {'form': form})

def edit_profile(request):
    form = EditProfileForm(request.POST or None, instance=request.user)
    if form.is_valid():
        form.save()
        return redirect('head:home')
    return render(request, 'edit_profile.html', {'form': form})
