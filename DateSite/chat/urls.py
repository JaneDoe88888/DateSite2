from django.urls import path, include
from . import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView
from chat import views


urlpatterns = [
    # path("", chat_views.chat_page, name="chat-page"),
    path('', views.get_chats, name='chats'),
    path('<int:chat_id>/', views.get_chat, name='chat'),
    path('', views.get_message, name='message'),


    # login-section
    path("auth/login/", LoginView.as_view(template_name="chat/LoginPage.html"), name="login-user"),
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
]
