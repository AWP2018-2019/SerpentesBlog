from django.conf.urls import url
from views import (
    index,
    PostListView,
    CommentCreateView,
    post_detail,
    UserProfileView,
)

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^$', PostListView.as_view(), name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/comment/create$', CommentCreateView.as_view(), name='comment_create'),
    url(r'^userprofile/(?P<pk>[0-9]+)$', UserProfileView.as_view(), name='user_profile'),
]