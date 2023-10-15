from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Chat(models.Model):
    members = models.ManyToManyField(User, related_name='chats')

    class Meta:
        verbose_name = 'чат'
        verbose_name_plural = 'чаты'

    def __str__(self):
        return str(self.id)


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='messages')
    content = models.CharField(max_length=500)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    pub_date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'

    def __str__(self):
        return str(self.id)