# Generated by Django 4.2.2 on 2023-10-16 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('head', '0013_news_author_alter_news_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]