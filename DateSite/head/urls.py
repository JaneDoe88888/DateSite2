from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('sign_out', views.sign_out, name='sign_out'),
    path('news/', views.news, name='news'),
    path('chat/', views.chat, name='chat'),
    path('friends/', views.friends, name='friends'),
    path('favorite/', views.favorite, name='favorite'),
    path('photo/', views.photo, name='photo'),
    path('settings/', views.settings, name='settings'),
    path('search/', views.search, name='search')
]





