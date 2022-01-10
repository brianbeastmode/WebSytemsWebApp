from django import forms
from main.models import UserProfile

class UpdateForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ("fullname", "bio", "profile_pic")