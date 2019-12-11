from django.conf import settings
from django.urls import path

from .feeds import LatestEntriesFeed
from .views import BlogDetailView, BlogListView, CommentDeleteView

COMMENTS_ENABLED = getattr(settings, 'BLOG_COMMENTS', False)

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('feed/', LatestEntriesFeed(), name='blog_feed'),
    path('<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
]

if COMMENTS_ENABLED:
    urlpatterns += [
        path('comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='blog_comment_delete')
    ]
