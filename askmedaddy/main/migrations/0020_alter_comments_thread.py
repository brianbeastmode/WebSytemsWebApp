# Generated by Django 3.2.9 on 2021-12-18 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20211218_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.thread'),
        ),
    ]
