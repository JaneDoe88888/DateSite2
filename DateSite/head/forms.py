from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from users.bulma_mixin import BulmaMixin

from .models import Image


class SignInForm(BulmaMixin, AuthenticationForm):
    username = forms.CharField(label='Введите имя пользоваться')
    password = forms.CharField(widget=forms.PasswordInput(),
                               label='Введите пароль')

    class Meta:
        model = User
        fields = ['username', 'password']


class UploadForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Image
        fields = ['image', ]
