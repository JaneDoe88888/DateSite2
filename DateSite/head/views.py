from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout
from .forms import *


def home(request):
    action = request.GET.get('action')
    confirm_login = False
    if action == 'log_in':
        confirm_login = True
    form = SignInForm(data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('head:profile', pk=user.pk)
    return render(request, 'home.html', {'form': form, 'confirm_login': confirm_login})

  
def profile(request, pk):
    user_pk = User.objects.get(pk=pk)
    account = UserProfile.objects.get(user=user_pk)
    form = PhotoProfile(request.POST or None,
                        request.FILES or None,
                        instance=account)
    action = request.GET.get('action')
    # act_ph = request.GET.get('act_ph')
    confirm_photo = False
    if action == 'photo':
        confirm_photo = True
        if form.is_valid():
            form.save()
            return redirect('head:profile', pk=pk)
    if action == 'delete':
        account.image = 'default-profile-photo.png'
        account.save()
    return render(request, 'profile.html', {'account': account, 'form': form, 
                                            'confirm_photo': confirm_photo})



def news(request):
    return render(request, 'news.html', {})


def chat(request):
    return render(request, 'chat.html', {})


def friends(request):
    return render(request, 'friends.html', {})


def favorite(request):
    return render(request, 'favorite.html')


def photo(request):
    return render(request, 'photo.html')


def settings(request):
    return render(request, 'settings.html', {})


def search(request):
    return render(request, 'search.html', {})


def sign_out(request):
    logout(request)
    return redirect('head:home')
