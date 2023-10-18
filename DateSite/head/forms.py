
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.validators import MinValueValidator
from users.bulma_mixin import BulmaMixin
from .models import *


from .models import Image


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


# class UploadForm(forms.ModelForm):
#     image = forms.ImageField()
#
#     class Meta:
#         model = Image
#         fields = ['image', ]


class SearchForm(BulmaMixin, forms.ModelForm):
    gender = forms.ChoiceField(label='Выберите пол', choices=GENDER)
    age_min = forms.IntegerField(label='Минимальный возраст')
    age_max = forms.IntegerField(label='Максимальный возраст')
    city = forms.CharField(label='Введите город', max_length=255)

    class Meta:
        model = Profile
        fields = [
            'gender',
            'age_min',
            'age_max',
            'city',
        ]


class PhotoUploadForm(BulmaMixin, forms.ModelForm):
    photos = forms.FileField(widget=forms.FileInput )

    class Meta:
        model = Image
        fields = ['photos']