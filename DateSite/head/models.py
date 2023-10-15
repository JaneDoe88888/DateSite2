from django.db import models
from django.contrib.auth.models import User


class SliderImage(models.Model):
    image = models.ImageField()

    def __str__(self):
        return f"Image #{self.pk}"


class Interests(models.Model):
    name = models.CharField(max_length=255)


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


class Like(models.Model):
    from_user = models.ForeignKey(User, related_name='like_from', on_delete=models.CASCADE, null=True)
    to_user = models.ForeignKey(User, related_name='like_to', on_delete=models.CASCADE, null=True)
    created_at = models.DateField(auto_now_add=True)


class Match(models.Model):
    user1 = models.ForeignKey(User, related_name='match_user1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name='match_user2', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class News(models.Model):
    image = models.ImageField()
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    comments = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='liked_news')



EDU_CHOICE = [
    ('Полное среднее', 'Полное среднее'),
    ('Среднее специальное', 'Среднее специальное'),
    ('Высшее', 'Высшее')
]

class ChatRoom(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'Комната {self.slug}'