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
    ('male', 'мужчина'),
    ('female', 'женщина'),
    ('trans', 'трансформер')
]

class Profile(models.Model):
    username = models.CharField(max_length=255)
    birthday = models.DateTimeField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    about = models.TextField()
    job = models.CharField(max_length=255)
    hobbies = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICE)
    image = models.ImageField()
    images = models.ForeignKey('head.Image', on_delete=models.CASCADE)


class Image(models.Model):
    image = models.ImageField()
