# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

# Create your models here.
class Post(models.Model):
    text = models.CharField(max_length=200)
    profile_id = models.ForeignKey(UserProfile, related_name='profile')
    created_by = models.ForeignKey(User, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} created by {} at {}".format(self.text, self.created_by.username, self.created_at)
        

class Image(models.Model):
    nume = models.CharField(max_length=200)
    image = models.FileField()
    post = models.ForeignKey(Post, related_name="images")
    added_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, related_name='images')
    
    
class Comment(models.Model):
    text = models.CharField(max_length=200)
    post = models.ForeignKey(Post, related_name="comments")
    created_by = models.ForeignKey(User, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} created by {} at {}".format(self.text, self.created_by.username, self.created_at)