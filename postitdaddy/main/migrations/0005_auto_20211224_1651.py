# Generated by Django 3.1.7 on 2021-12-24 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_thread_community'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='community',
        ),
        migrations.AddField(
            model_name='thread',
            name='community',
            field=models.ManyToManyField(to='main.Community'),
        ),
    ]
