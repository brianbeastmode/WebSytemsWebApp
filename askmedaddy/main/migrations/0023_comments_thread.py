# Generated by Django 3.2.9 on 2021-12-18 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_remove_comments_thread'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='thread',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.thread'),
        ),
    ]
