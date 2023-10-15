import requests
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout
from .forms import SignInForm, EditProfileForm, SearchForm


def home(request):
    action = request.GET.get('action')
    confirm_login = False
    if action == 'log_in':
        confirm_login = True
    form = SignInForm(data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        profile_data = Profile.objects.filter(user__username=user.username)
        login(request, user)
        if not profile_data:
            Profile.objects.create(user=user, username=form.data['username'])
        return redirect('head:profile', pk=user.pk)
    return render(request, 'home.html', {'form': form, 'confirm_login': confirm_login})


def profile(request, pk):
    account = Profile.objects.get(user__username=request.user.username)
    return render(request, 'profile.html', {'account': account})


def edit_profile(request):
    account = Profile.objects.get(user__username=request.user.username)
    action = request.GET.get('action')
    confirm_edit = False
    profile_data = Profile.objects.get(user__username=request.user.username)
    form = EditProfileForm(data=request.POST or None, instance=profile_data)

    if action == 'edit_profile':
        confirm_edit = True
    if form.is_valid():
        form.save()
        return redirect('head:profile', pk=account.pk)
    return render(request, 'profile.html', {'form': form, 'confirm_edit': confirm_edit, 'account': profile_data})


def search(request):
    form = SearchForm(request.POST or None)
    if request.method == 'POST':
        form = SearchForm(request.POST or None)
        if form.is_valid():
            gender = form.data['gender']
            age_min = form.data['age_min']
            age_max = form.data['age_max']
            city = form.data['city']

            users = Profile.objects.filter(
                gender=gender,
                birthday__in=range(int(age_min), int(age_max) + 1),
                city=city
            )
            return render(request, 'search.html', {'users': users})
    return render(request, 'search.html', {'form': form})


def news(request):
    return render(request, 'news.html', {})


def friends(request):
    return render(request, 'friends.html', {})


def photo(request):
    return render(request, 'photo.html')


def settings(request):
    return render(request, 'settings.html', {})


def sign_out(request):
    logout(request)
    return redirect('head:home')
