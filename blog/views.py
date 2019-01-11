# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from models import Post
# Create your views here.

def index(request):
    post_list = Post.objects.all()
    return render(request, 'index.html', {'post_list': post_list})
    
class PostListView(ListView):
    template_name = 'index.html'
    model = Post
    context_object_name = 'post_list'