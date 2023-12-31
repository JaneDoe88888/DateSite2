# Generated by Django 4.2.2 on 2023-09-12 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('head', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('about', models.TextField()),
                ('job', models.CharField(max_length=255)),
                ('hobbies', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('birthday', models.DateTimeField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('men', 'men'), ('female', 'female')], max_length=255)),
            ],
        ),
    ]
