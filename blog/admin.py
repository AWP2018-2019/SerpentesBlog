# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
        list_display = ('text', 'created_by', 'post')

class UserProfileAdmin(admin.ModelAdmin):
        list_display =('user', 'birthday','last_name','first_name')
        search_fields=('user__username',)
        
admin.site.register(models.UserProfile, UserProfileAdmin)
admin.site.register(models.Post)
admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.Image)