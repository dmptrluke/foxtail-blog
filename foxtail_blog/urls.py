from django.conf import settings
from django.urls import path

from . import views

COMMENTS_ENABLED = getattr(settings, 'BLOG_COMMENTS', False)

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog_list'),
    path('<slug:slug>/', views.BlogDetailView.as_view(), name='blog_detail'),
]

if COMMENTS_ENABLED:
    urlpatterns += [
        path('comment/delete/<int:pk>/', views.CommentDeleteView.as_view(), name='blog_comment_delete')
    ]
