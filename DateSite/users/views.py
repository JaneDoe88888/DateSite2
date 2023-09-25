from django.shortcuts import render, redirect
from .forms import *
from head.models import UserProfile
from django.contrib.auth import login, logout

def sign_up(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
      user = form.save()
      UserProfile.objects.create(user=user)
      return redirect('head:home')
    return render(request, 'sign_up.html', {'form': form})