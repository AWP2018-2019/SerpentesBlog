# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from models import Post, Comment, UserProfile, Image, User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from forms import CommentForm,UserProfileForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from datetime import datetime 


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
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['text']
    template_name = 'post_create.html'

    def form_valid(self, form):
        post = Post.objects.create(
            created_by=self.request.user,
            **form.cleaned_data
        )
        return redirect(reverse_lazy("post_detail", kwargs={"pk": post.id }))

class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['text']
    template_name = 'post_update.html'

    def form_valid(self, form):
        post = Post.objects.get(pk=self.kwargs['pk'])
        post.text = form.cleaned_data['text']
        post.save()
        return redirect(reverse_lazy("post_detail", kwargs={"pk": self.kwargs['pk']}))
        
class PostDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "post_delete.html"
    model = Post

    def get_success_url(self):
        return reverse_lazy('index')
    
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
        
class CommentEditView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ['text']
    pk_url_kwarg = 'pk_comment'
    template_name = 'comment_update.html'

    def form_valid(self, form):
        comment = Comment.objects.get(pk=self.kwargs['pk_comment'])
        comment.text = form.cleaned_data['text']
        comment.save()
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
        
class UserProfileCreateView( CreateView):
    model = UserProfile
    fields = ['birthday', 'first_name', 'last_name']
    template_name = 'user_profile_create.html'
    
    
    def form_valid(self, form):
        UserProfile.objects.create(
            user=self.request.user,
            **form.cleaned_data
        )
        return redirect(reverse_lazy("index"))
        
class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'profile_update.html'

    def get_context_data(self, **kwargs):
        context = super(UserProfileUpdateView, self).get_context_data(**kwargs)
        user =  self.object.user
        context['form'].fields['first_name'].initial = user.first_name
        context['form'].fields['last_name'].initial = user.last_name
        context['form'].fields['e_mail'].initial = user.email
        return context

    def form_valid(self, form):
        data = form.cleaned_data
        self.object.birthday = data['birthday']
        self.request.user.first_name = data['first_name']
        self.request.user.last_name = data['last_name']
        self.request.user.email = data['e_mail']
        self.object.save()
        self.request.user.save()
        return redirect(reverse_lazy("user_profile",
                                     kwargs={"pk": self.request.user.id}))


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

    def post(self, request, *args, **kwargs):
        form = UserCreationForm( data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(username=data['username'],
                                        password=data['password1'])
            #UserProfile.objects.create(user=user)
            # import pdb; pdb.set_trace()
            user = authenticate(username=data['username'], password=data['password1'])
            login(request, user)
            return redirect(reverse_lazy("user_profile_create",
                                     kwargs={"pk": user.id}))
        else:
            return redirect('index')
        

class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse_lazy('index'))
        
class UploadImage(CreateView): 
    model = Image
    fields = ['nume','image']
    template_name = 'image_upload.html'

        
    def post(self, request, *args, **kwargs):
        # import pdb; pdb.set_trace()
        post = Post.objects.get(id = self.kwargs['pk'])
        Image.objects.create(
            added_by = self.request.user,
            post = post,
            image = request.FILES['image_path'])
        return redirect(reverse_lazy("post_detail", kwargs={"pk": self.kwargs['pk']}))
