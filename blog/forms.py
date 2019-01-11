from django import forms
from blog import models

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['text']