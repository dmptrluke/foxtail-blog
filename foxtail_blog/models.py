from django.conf import settings
from django.db import models
from django.urls import reverse

from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_CLASSY
from taggit.managers import TaggableManager
from versatileimagefield.fields import PPOIField, VersatileImageField


class Post(models.Model):
    title = models.CharField(max_length=100, help_text="100 characters or fewer.")
    slug = models.SlugField(unique=True, help_text="Changing this value after initial creation will break existing "
                                                   "post URLs. Must be unique.")
    tags = TaggableManager(blank=True)

    allow_comments = models.BooleanField(default=True)

    author = models.CharField(max_length=50, help_text="50 characters or fewer.")
    created = models.DateTimeField(auto_now_add=True, verbose_name="date created")
    modified = models.DateTimeField(auto_now=True, verbose_name="date modified")

    image = VersatileImageField(upload_to='blog', blank=True, null=True, ppoi_field='image_ppoi')
    image_ppoi = PPOIField()

    text = MarkdownField(rendered_field='text_rendered', validator=VALIDATOR_CLASSY)
    text_rendered = RenderedMarkdownField()

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})


class Comment(models.Model):
    post = models.ForeignKey('foxtail_blog.Post',
                             on_delete=models.CASCADE, related_name='comments')

    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE, )

    text = models.TextField(max_length=280, help_text="280 characters or fewer.")
    created_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.text
