from django.db import models
from django.contrib.auth.models import User


class SliderImage(models.Model):
    image = models.ImageField()

    def __str__(self):
        return f"Image #{self.pk}"


GENDER = [
    ('men', 'men'),
    ('female', 'female'),
    ('trans', 'трансформер')
]

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

# class User(models.Model):
#     username = models.CharField(max_length=255)
#     birthday = models.DateTimeField()
#     email = models.EmailField()
#     password = models.CharField(max_length=255)
#     gender = models.CharField(max_length=255, choices=GENDER_CHOICE)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default-profile-photo.png', blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    birthday = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    job = models.CharField(max_length=255, null=True, blank=True)
    hobbies = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, choices=GENDER, blank=True)
    friends = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.user.username


# class Profile(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     city = models.CharField(max_length=255)
#     about = models.TextField()
#     job = models.CharField(max_length=255)
#     hobbies = models.CharField(max_length=255)
#     image = models.ImageField()