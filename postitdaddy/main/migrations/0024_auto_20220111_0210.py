# Generated by Django 3.1.7 on 2022-01-10 18:10

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20220107_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default=None, force_format=None, keep_meta=True, null=True, quality=100, size=[25, 25], upload_to='user_pic'),
        ),
    ]