from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

# Create your models here.
class Tags(models.Model):
    tagName = models.CharField(max_length=20)

class Comments(models.Model):
    content = models.TextField()
    votes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='commentVoter')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank = True)


class Thread(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True)
    tags = models.ManyToManyField('Tags')
    comments = models.ForeignKey('Comments', on_delete=models.CASCADE, null=True, blank = True)
    date = models.DateField(auto_now_add=True)
    votes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='postVoter')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    