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
    account = Profile.objects.get(user__username=request.user.username)
    return render(request, 'profile.html', {'account': account})


def edit_photo(request):
    account = Profile.objects.get(user__username=request.user.username)
    form = PhotoProfile(request.POST or None,
                        request.FILES or None,
                        instance=account)

    action = request.GET.get('action')
    confirm_photo = False

    if action == 'photo':
        confirm_photo = True
        if form.is_valid():
            form.save()
            return redirect('head:profile', pk=account.pk)
    if action == 'delete':
        account.image = 'default-profile-photo.png'
        account.save()

    return render(request, 'profile.html', {'account': account, 'form': form, 'confirm_photo': confirm_photo})


def edit_about(request):
    account = Profile.objects.get(user__username=request.user.username)

    about_me_form = AboutMeProfile(request.POST or None, instance=account)
    action = request.GET.get('action')
    confirm_about = False

    if action == 'about_me':
        confirm_about = True
        if about_me_form.is_valid():
            account.save()
            return redirect('head:profile', pk=account.pk)

    return render(request, 'profile.html',
                  {'account': account, 'about_me_form': about_me_form, 'confirm_about': confirm_about})

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

def news(request):
    account = Profile.objects.get(user__username=request.user.username)
    return render(request, 'news.html', {'account': account})


def chat(request):
    account = Profile.objects.get(user__username=request.user.username)
    return render(request, 'chat.html', {'account': account})


def friends(request):
    account = Profile.objects.get(user__username=request.user.username)
    action = request.GET.get('action')
    if action:
        account.friends.add(request.user)\
            if request.user not in account.friends.all() \
            else account.friends.remove(request.user)
        # return redirect()
    my_friends = account.friends.all()
    return render(request, 'friends.html', {'account': account, 'friends': my_friends})


def favorite(request):
    account = Profile.objects.get(user__username=request.user.username)
    return render(request, 'favorite.html', {'account': account})


def photo(request):
    account = Profile.objects.get(user__username=request.user.username)
    return render(request, 'photo.html', {'account': account})


def settings(request):
    account = Profile.objects.get(user__username=request.user.username)
    return render(request, 'settings.html', {'account': account})


def search(request):
    account = Profile.objects.get(user__username=request.user.username)
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
            print(users)
            
            return render(request, 'search.html', {'users': users})
    return render(request, 'search.html', {'account': account, 'form': form})


def sign_out(request):
    logout(request)
    return redirect('head:home')
 