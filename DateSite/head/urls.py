from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('profile/<pk>', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('sign_out', views.sign_out, name='sign_out'),
    path('photo/', views.photo, name='photo'),
    path('settings/', views.settings, name='settings'),
    path('search/', views.search, name='search'),
    path('found/', views.found, name='found'),

]
