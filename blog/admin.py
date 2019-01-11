# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
        list_display = ('text', 'created_by', 'post')

admin.site.register(models.Post)
admin.site.register(models.Comment, CommentAdmin)