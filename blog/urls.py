from django.conf.urls import url
from views import (
    index,
    PostListView,
    CommentCreateView,
    CommentEditView,
    CommentDeleteView,
    post_detail,
    PostCreateView,
    PostEditView,
    PostDeleteView,
    UserProfileView,
    UserProfileUpdateView,
    LoginView,
    RegisterView,
    LogoutView,
    
)

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^$', PostListView.as_view(), name='post_list'),
    url(r'^post/create$', PostCreateView.as_view(), name='post_create'),
    url(r'^post/(?P<pk>[0-9]+)/edit$', PostEditView.as_view(), name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/delete$', PostDeleteView.as_view(), name='post_delete'),
    url(r'^post/(?P<pk>[0-9]+)/comment/create$', CommentCreateView.as_view(), name='comment_create'),
    url(r'^userprofile/(?P<pk>[0-9]+)$', UserProfileView.as_view(), name='user_profile'),
    url(r'^userprofile/(?P<pk>[0-9]+)/edit$', UserProfileUpdateView.as_view(),name='profile_edit'),
    url(r'^post/(?P<pk>[0-9]+)/comment/(?P<pk_comment>[0-9]+)/edit$', CommentEditView.as_view(), name='comment_edit'),
    url(r'^post/(?P<pk>[0-9]+)/comment/(?P<pk_comment>[0-9]+)/delete$', CommentDeleteView.as_view(), name='comment_delete'),
]