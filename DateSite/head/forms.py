from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import *
from users.bulma_mixin import BulmaMixin
from django.core.validators import MinValueValidator

class SignInForm(BulmaMixin, AuthenticationForm):
    username = forms.CharField(label='Введите имя пользоваться')
    password = forms.CharField(widget=forms.PasswordInput(),
                               label='Введите пароль')
    
    class Meta:
        model = User
        fields = ['username', 'password']

class PhotoProfile(forms.ModelForm):
    image = forms.ImageField(label='Загрузите фотографию')

    class Meta:
        model = Profile
        fields = ['image',]

class AboutMeProfile(forms.ModelForm, BulmaMixin):
    about = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'textarea'
    }), label='Расскажите о себе', required=False)

    class Meta:
        model = Profile
        fields = ['about',]

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

class EditProfileForm(BulmaMixin, forms.ModelForm):
    gender = forms.ChoiceField(label='Выберите пол', choices=GENDER)
    birthday = forms.IntegerField(label='Ваш возраст', validators=[MinValueValidator(limit_value=18)], required=False)
    city = forms.CharField(label='Ваш город', required=False)
    job = forms.CharField(label='Ваша работа', required=False)
    hobbies = forms.CharField(label='Ваше хобби', required=False)

    class Meta:
        model = Profile
        fields = [
            'birthday',
            'city',
            'job',
            'hobbies',
            'gender'
        ]