from django.conf.urls import url
from views import (
    index,
    PostListView,
    CommentCreateView,
    CommentDeleteView,
    post_detail,
    UserProfileView,
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
    url(r'^post/(?P<pk>[0-9]+)/comment/create$', CommentCreateView.as_view(), name='comment_create'),
    url(r'^userprofile/(?P<pk>[0-9]+)$', UserProfileView.as_view(), name='user_profile'),
    url(r'^post/(?P<pk>[0-9]+)/comment/(?P<pk_comment>[0-9]+)/delete$', CommentDeleteView.as_view(), name='comment_delete'),
]