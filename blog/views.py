# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from models import Post, Comment, UserProfile, Image, User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from forms import CommentForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


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
        
class CommentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "comment_delete.html"
    model = Comment
    pk_url_kwarg = 'pk_comment'

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"pk": self.kwargs['pk']})


class UserProfileView(LoginRequiredMixin, DetailView):
    template_name = 'userprofile.html'
    model = UserProfile
    context_object_name = 'userprofile'

    def get_object(self):
        user = User.objects.get(id=self.kwargs['pk'])
        return user

class LoginView(TemplateView):
    template_name = 'login.html'

    def get_context_data(self):
        form = AuthenticationForm()
        return {'form': form}

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'],
                                password=data['password'])
            login(request, user)
            return redirect(reverse_lazy('index'))
        else:
            return render(request, "login.html", {"form": form})

class RegisterView(CreateView):
    template_name= 'register.html'
    form_class = UserCreationForm
    model = User

    def form_valid(self, form):
        data = form.cleaned_data
        user = User.objects.create_user(username=data['username'],
                                        password=data['password1'])
        UserProfile.objects.create(user=user)
        return redirect('index')

class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse_lazy('index'))