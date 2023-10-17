from django.db import models
from django.contrib.auth.models import User


class SliderImage(models.Model):
    image = models.ImageField()

    def __str__(self):
        return f"Image #{self.pk}"


GENDER = [
    ('', ''),
    ('мужчина', 'мужчина'),
    ('женщина', 'женщина'),
    ('трансформер', 'trans')
]

STATUS_CHOICE = [
    ('', '---'),
    ('В активном поиске', 'В активном поиске'),
    ('Влюблен(а)', 'Влюблен(а)'),
    ('Встречается', 'Встречается'),
    ('В гражданском браке', 'В гражданском браке'),
    ('Помолвлен(а)', 'Помолвлен(а)'),
    ('Женат(Замужем)', 'Женат(Замужем)'),
    ('Все сложно', 'Все сложно'),
    ('Не женат(Не замужем)', 'Не женат(Не замужем)')
]


class Profile(models.Model):
    user_name = models.CharField(max_length=255, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.IntegerField(blank=True, null=True)
    biography = models.TextField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    job = models.CharField(max_length=255, null=True, blank=True)
    hobbies = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(default='default-profile-photo.png', blank=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICE, blank=True)
    gender = models.CharField(max_length=255, choices=GENDER, blank=True)

    def __str__(self):
        return self.user.username
