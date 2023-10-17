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
    # user_pk=User.objects.get(pk=pk)
    # account = Profile.objects.get(pk=user_pk)
    # action=request.GET.get('action')
    account = Profile.objects.get(user__pk=pk)
    # if not account.user_name:
    #     account.user_name = account.user.username
    #     account.save()
    # if action:
    #     add_remove_friends(request)
    #     return redirect('head:friends')
    return render(request, 'profile.html', {'account': account})


def edit_photo(request):
    account = Profile.objects.get(user__username=request.user.username)
    form = PhotoProfileForm(request.POST or None,
                        request.FILES or None,
                        instance=account)

    action = request.GET.get('action')
    confirm_photo = False

    if action == 'photo':
        confirm_photo = True
        if form.is_valid():
            form.save()
            return redirect('head:profile', pk=request.user.pk)
    if action == 'delete':
        account.image = 'default-profile-photo.png'
        account.save()
        print(account.image)
    return render(request, 'profile.html', {'account': account, 'form': form, 'confirm_photo': confirm_photo})


def edit_about(request):
    account = Profile.objects.get(user__username=request.user.username)

    about_me_form = AboutMeProfileForm(request.POST or None, instance=account)
    action = request.GET.get('action')
    confirm_about = False

    if action == 'about_me':
        confirm_about = True
        if about_me_form.is_valid():
            account.save()
            return redirect('head:profile', pk=request.user.pk)

    return render(request, 'profile.html',
                  {'account': account, 'about_me_form': about_me_form, 'confirm_about': confirm_about})

def edit_profile(request):
    # account = Profile.objects.get(user__username=request.user.username)
    action = request.GET.get('action')
    confirm_edit = False
    profile_data = Profile.objects.get(user__username=request.user.username)
    form = EditProfileForm(data=request.POST or None, instance=profile_data)
    if action == 'edit_profile':
        confirm_edit = True
    if form.is_valid():
        form.save()
        return redirect('head:profile', pk=request.user.pk)
    return render(request, 'profile.html', {'form': form, 'confirm_edit': confirm_edit, 'account': profile_data})

def news(request):
    account = Profile.objects.get(user__username=request.user.username)
    return render(request, 'news.html', {'account': account})


def chat(request):
    account = Profile.objects.get(user__username=request.user.username)
    return render(request, 'chat.html', {'account': account})

def add_remove_friends(request):
    account = Profile.objects.get(user__username=request.user.username)
#     acc_pk = request.GET.get('pk') if not pk else pk
    # user_pk = User.objects.get(pk=pk)
    # account = Profile.objects.get(user=user_pk)
    account=account.friends.add(request.user)\
        if request.user not in account.friends.all()\
        else account.friends.remove(request.user)
        # return redirect('head:friends', pk=account.pk)

def my_friends(request, pk):
    # acc_pk = request.GET.get('pk') if not pk else pk
    # user_pk = User.objects.get(pk=pk)
    # account = Profile.objects.get(user=user_pk)
    account = Profile.objects.get(user__username=request.user.username)
    # account = Friend.objects.filter(user__username=request.user.username)

    action = request.GET.get('action')
    if action:
        add_remove_friends(request)
    #     # add_remove_friends(request)
    #     # return redirect('head:friends')
    #     account=account.friends.add(request.user)\
    #     if request.user not in account.friends.all() and not request.user.is_authenticated\
    #     else account.friends.remove(request.user)
        return redirect('head:friends', pk=account.pk)
    # mfriends = account.friends.all()
    # print(account.friends.all())
    return render(request, 'friends.html', {'account': account})

def add_friend(request, pk):
    user_pk = User.objects.get(pk=pk)
    my_friend = Profile.objects.get(user=user_pk)
#     my_friend = Profile.objects.get(user__username=request.user.username)
#     FriendRequest.objects.create(friend=my_friend)
    
# def my_requests(request, pk):
#     user_pk = User.objects.get(pk=pk)
#     my_requests = FriendRequest.objects.filter(user=user_pk)
#     return render(request, 'my_requests.html', {'my_requests': my_requests})
# def friend_requests(request):
#     requests = FriendRequest.objects.all()
#     action = request.GET.get('action')
#     pk = request.GET.get('pk')
#     if action == ''


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
    # user_pk = User.objects.get(pk=pk)
    # account = Profile.objects.get(user=user_pk)
    account = Profile.objects.get(user__username=request.user.username)
    # action = request.GET.get('action')
    # pk = request.GET.get('pk')
    # if action == 'friend':
    #     add_remove_friends(request)
    #     return redirect('head:search')
    form = SearchForm(request.POST or None)
    profiles = []
    if request.method == 'POST':
        
        if form.is_valid():
            gender = form.data['gender'] 
            age_min = form.data['age_min'] if form.data['age_min'] else 18
            age_max = form.data['age_max'] if form.data['age_max'] else 99
            city = form.data['city'] 

            if city:
                profiles = Profile.objects.filter(
                gender=gender,
                birthday__in=range(int(age_min), int(age_max) + 1),
                city=city 
                )
            else:
                profiles = Profile.objects.filter(
                gender=gender,
                birthday__in=range(int(age_min), int(age_max) + 1)
                )
            
    return render(request, 'search.html', {'account': account, 'form': form, 'profiles': profiles})

def sign_out(request):
    logout(request)
    return redirect('head:home')
 