# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from forms import CommentForm


def index(request):
    post_list = Post.objects.all()
    return render(request, 'index.html', {'post_list': post_list})

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    form = CommentForm()
    return render(request, "post_detail.html", 
    {"post": post, "form": form})
    
class PostListView(ListView):
    template_name = 'index.html'
    model = Post
    context_object_name = 'post_list'
    
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['text']
    
    def form_valid(self, form):
        post = Post.objects.get(id=self.kwargs['pk'])
        Comment.objects.create(
            created_by=self.request.user,
            post=post,
            **form.cleaned_data
        )
        return redirect(reverse_lazy("post_detail", kwargs={"pk": self.kwargs['pk']}))