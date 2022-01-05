from django import forms
from django.forms import ModelForm


from .models import Thread, Community

class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        fields = ('title', 'content', 'tags', 'community')

class CommunityForm(ModelForm):
    class Meta:
        model = Community
        fields = ('title',)