from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, logout

def sign_up(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
       form.save()
       return redirect('head:home')
    return render(request, 'sign_up.html', {'form': form})