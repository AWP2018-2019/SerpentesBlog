from django import forms
from blog import models

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['text']
        
class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    e_mail = forms.CharField(max_length=100)
    class Meta:
        model =models.UserProfile
        exclude = ['user']


