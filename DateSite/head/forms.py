from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.validators import MinValueValidator
from users.bulma_mixin import BulmaMixin
from .models import *


class SignInForm(BulmaMixin, AuthenticationForm):
    username = forms.CharField(label='Введите имя пользоваться')
    password = forms.CharField(widget=forms.PasswordInput(),
                               label='Введите пароль')

    class Meta:
        model = User
        fields = ['username', 'password']

class EditProfileForm(BulmaMixin, forms.ModelForm):
    username = forms.CharField(label='Введите имя')
    birthday = forms.IntegerField(label='Ваш возраст', validators=[MinValueValidator(limit_value=18)])
    city = forms.CharField(label='Ваш город')
    job = forms.CharField(label='Ваша работа')
    hobbies = forms.CharField(label='Ваше хобби')
    status = forms.ChoiceField(label='Ваше семейное положение', choices=STATUS_CHOICE)

    class Meta:
        model = Profile
        fields = [
            'username',
            'birthday',
            'city',
            'job',
            'hobbies',
            'status'
        ]
