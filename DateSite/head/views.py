from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout
from .forms import SignInForm, UploadForm


def home(request):
    action = request.GET.get('action')
    confirm_login = False
    if action == 'log_in':
        confirm_login = True
    form = SignInForm(data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('head:profile')
    return render(request, 'home.html', {'form': form, 'confirm_login': confirm_login})


def profile(request):
    return render(request, 'profile.html', {})


def news(request):
    return render(request, 'news.html', {})


def chat(request):
    return render(request, 'chat.html', {})


def friends(request):
    return render(request, 'friends.html', {})


def favorite(request):
    return render(request, 'favorite.html')


def photo(request):
    form = UploadForm(request.POST or None, request.FILES or None)
    if form.is_valid():

        profile_data = Profile.objects.get(pk=request.POST.get('pk'))
        print(request.POST)

    return render(request, 'photo.html', {'form': form})


def settings(request):
    return render(request, 'settings.html', {})


def search(request):
    return render(request, 'search.html', {})


def sign_out(request):
    logout(request)
    return redirect('head:home')

#
# def upload(request, pk):
#     profile_data = Profile.objects.get(pk=pk)
#     print(request.POST)
#     return  redirect('head:profile')
