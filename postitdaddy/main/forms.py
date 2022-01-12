from django import forms
from django.forms import ModelForm


from .models import Thread, Community

class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        fields = ('title', 'content', 'tags', 'image', 'community', )
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title', 'type': 'text'}),
            'content' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Text(optional)'}),
            'community' : forms.Select(attrs={'class': 'form-control',}),
            'tags' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Put comma in between tags'}),
            'image' : forms.ClearableFileInput(attrs={'class': 'form-control-file', 'type': 'file', 'accept': "image/*"}),
        }

class CommunityForm(ModelForm):
    class Meta:
        model = Community
        fields = ('title',)
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Community Name', 'type': 'text'}),
        }