# Generated by Django 3.1.7 on 2022-01-06 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20220107_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='comment',
            field=models.ManyToManyField(blank=True, to='main.Comment'),
        ),
    ]