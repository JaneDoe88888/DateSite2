from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('edit_photo', views.edit_photo, name='edit_photo'),
    path('edit_about', views.edit_about, name='edit_about'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('sign_out', views.sign_out, name='sign_out'),
    path('news/', views.news, name='news'),
    path('chat/', views.chat, name='chat'),
    path('friends/<int:pk>', views.my_friends, name='friends'),
    path('my_requests/<int:pk>', views.add_friend, name='my_requests'),
    path('favorite/', views.favorite, name='favorite'),
    path('photo/', views.photo, name='photo'),
    path('settings/', views.settings, name='settings'),
    path('search/', views.search, name='search')
]




