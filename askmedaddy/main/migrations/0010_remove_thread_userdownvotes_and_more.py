# Generated by Django 4.0 on 2021-12-14 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_rename_post_thread'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='userDownVotes',
        ),
        migrations.RemoveField(
            model_name='thread',
            name='userUpVotes',
        ),
    ]