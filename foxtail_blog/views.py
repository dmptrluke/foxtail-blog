from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.db.models import Count
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView

from .forms import CommentForm
from .models import Post, Comment


class BlogListView(ListView):
    model = Post
    paginate_by = 10
    context_object_name = 'posts'
    template_name = 'blog/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sidebar_post_list'] = Post.objects.all()[:5]
        context['sidebar_tag_list'] = Post.tags.annotate(num_times=Count('taggit_taggeditem_items'))
        return context

    def get_queryset(self):
        q = self.request.GET.get('q')
        tag = self.request.GET.get('tag')

        if q:
            # user is doing a search query
            query = SearchQuery(q)
            vector = SearchVector('text', 'title')
            queryset = self.model.objects.annotate(rank=SearchRank(vector, query)) \
                .prefetch_related('tags') \
                .order_by('-rank')

        elif tag:
            # user is doing a tag query
            queryset = self.model.objects \
                .prefetch_related('tags') \
                .filter(tags__slug__in=[tag])
        else:
            queryset = self.model.objects.prefetch_related('tags').all()

        return queryset


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    queryset = Post.objects.prefetch_related('comments__author').prefetch_related('tags').all()

    def get_context_data(self, form=CommentForm(), **kwargs):
        context = super().get_context_data(**kwargs)
        context['sidebar_post_list'] = Post.objects.all()[:5]
        context['sidebar_tag_list'] = Post.tags.most_common()[:8]
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()

        post = self.get_object()

        if not post.allow_comments:
            return HttpResponseForbidden()

        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(self.request, 'Your comment has been posted!')
            return redirect('blog_detail', slug=post.slug)
        else:
            messages.error(self.request, 'There was a problem posting your comment.')
            context = self.get_context_data(form=form, object=post)

        return self.render_to_response(context)


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_delete.html'

    def delete(self, request, *args, **kwargs):
        comment = self.get_object()

        if not (comment.author == request.user or request.user.has_perm('foxtail_blog.delete_comment')):
            return HttpResponseForbidden()

        slug = comment.post.slug
        comment.delete()
        messages.success(self.request, 'Your comment has been deleted.')
        return redirect('blog_detail', slug=slug)
