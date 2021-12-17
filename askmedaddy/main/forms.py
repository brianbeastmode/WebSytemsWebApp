from django import forms
from django.forms import ModelForm


from .models import Thread, Comments

class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        fields = ('title', 'content', 'tags',)
        exclude  = ['user']

class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('content',)