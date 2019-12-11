from django.contrib.syndication.views import Feed
from django.utils.html import strip_tags

from .models import Post


class LatestEntriesFeed(Feed):
    title = "Latest News"
    link = "/blog/"
    description = "Updates from furry.nz."

    def items(self):
        return Post.objects.order_by('-created')[:20]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return strip_tags(item.text_rendered)

    def item_pubdate(self, item):
        return item.created


__all__ = ['LatestEntriesFeed']
