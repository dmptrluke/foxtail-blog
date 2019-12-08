from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.db.models import TextField
from django.forms import Textarea
from django.template.defaultfilters import truncatechars
from django.urls import reverse
from django.utils.html import format_html

from .models import Post, Comment


class PostAdmin(ModelAdmin):
    fieldsets = (
        ('Content', {
            'fields': ('title', 'tags', 'author', 'text')
        }),
        ('Image', {
            'fields': ('image',),
        }),
        ('Advanced options', {
            'fields': ('slug', 'allow_comments'),
        }),
    )

    formfield_overrides = {
        TextField: {'widget': Textarea(attrs={'rows': 40, 'cols': 120})},
    }

    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('created', 'tags', 'author')
    list_display = ('title', 'tag_list', 'created', 'modified', 'author')

    @staticmethod
    def tag_list(obj):
        return ", ".join(o.name for o in obj.tags.all().order_by('name'))


class CommentAdmin(ModelAdmin):
    list_display = ('text_preview', 'post_link', 'author', 'created_date')

    def post_link(self, obj):
        return format_html('<a href="{}">{}</a>',
                           reverse("admin:foxtail_blog_post_change", args=(obj.post.pk,)),
                           obj.post.title)

    def text_preview(self, obj):
        return truncatechars(obj.text, 50)

    text_preview.short_description = "Comment"
    post_link.short_description = "Post"


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
