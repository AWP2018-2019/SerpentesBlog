from django.conf.urls import url
from views import (
    index,
    PostListView,
)

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^$', PostListView.as_view(), name='post_list'),
]