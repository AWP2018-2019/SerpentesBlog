from django.conf.urls import url
from views import (
    index,
    PostListView,
    CommentCreateView,
    post_detail,
)

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^$', PostListView.as_view(), name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/comment/create$', CommentCreateView.as_view(), name='comment_create'),
]