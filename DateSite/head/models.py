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


  #   email = models.EmailField()
   #  password = models.CharField(max_length=255)



STATUS_CHOICE = [
    ('В активном поиске', 'В активном поиске'),
    ('Влюблен(а)', 'Влюблен(а)'),
    ('Встречается', 'Встречается'),
    ('В гражданском браке', 'В гражданском браке'),
    ('Помолвлен(а)', 'Помолвлен(а)'),
    ('Женат(Замужем)', 'Женат(Замужем)'),
    ('Все сложно', 'Все сложно'),
    ('Не женат(Не замужем)', 'Не женат(Не замужем)')
]
GENDER = [
    ('---', '---'),
    ('male', 'мужчина'),
    ('female', 'женщина'),
    ('trans', 'трансформер')
]

class Profile(models.Model):
    username = models.CharField(User, max_length=255, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    birthday = models.IntegerField(blank=True, null=True)
    biography = models.TextField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    job = models.CharField(max_length=255, blank=True, null=True)
    hobbies = models.CharField(max_length=255, null=True)
    image = models.ImageField(blank=True, null=True, default=None)
    status = models.CharField(max_length=255, choices=STATUS_CHOICE)
    gender = models.CharField(max_length=255, choices=GENDER)

    def __str__(self):
        return self.user.username

class Image(models.Model):
    image = models.ImageField()

#
# class UploadPhotos(models.Model):
#     photos = models.ImageField()
