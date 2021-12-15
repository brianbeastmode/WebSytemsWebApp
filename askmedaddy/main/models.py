from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True)

    def __str__(self):
        return str(self.user)   

class Tags(models.Model):
    tagName = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.tagName

class Comments(models.Model):
    content = models.TextField()
    votes = models.ManyToManyField(User, related_name='commentVoter')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank = True)

    class Meta:
        verbose_name_plural = 'Comments'

class Thread(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True)
    tags = models.ManyToManyField('Tags')
    comments = models.ForeignKey('Comments', on_delete=models.CASCADE, null=True, blank = True)
    votes = models.ManyToManyField(User, related_name='postVoter')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)    

    class Meta:
        verbose_name_plural = 'Threads'

    def __str__(self):
        return self.title