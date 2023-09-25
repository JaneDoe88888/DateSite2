from django.db import models
from django.contrib.auth.models import User


class SliderImage(models.Model):
    image = models.ImageField()

    def __str__(self):
        return f"Image #{self.pk}"


GENDER_CHOICE = [
    ('men', 'men'),
    ('female', 'female')
]


# class User(models.Model):
#     username = models.CharField(max_length=255)
#     birthday = models.DateTimeField()
#     email = models.EmailField()
#     password = models.CharField(max_length=255)
#     gender = models.CharField(max_length=255, choices=GENDER_CHOICE)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default-profile-photo.png', blank=True)

    def __str__(self):
        return self.user.username


class Profile(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    about = models.TextField()
    job = models.CharField(max_length=255)
    hobbies = models.CharField(max_length=255)
    image = models.ImageField()