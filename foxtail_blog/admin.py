from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.template.defaultfilters import truncatechars
from django.urls import reverse
from django.utils.html import format_html

from published.admin import PublishedAdmin
from published.admin_helpers import add_to_fieldsets, add_to_list_display, add_to_readonly_fields

from .models import Comment, Post


class PostAdmin(PublishedAdmin):
    fieldsets = (
        ('Content', {
            'fields': ('title', 'tags', 'author', 'text')
        }),
        add_to_fieldsets(section=True, collapse=False),
        ('Image', {
            'fields': ('image',),
        }),
        ('Advanced options', {
            'fields': ('slug', 'allow_comments'),
        }),
    )

    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = add_to_readonly_fields()
    list_filter = ('created', 'tags', 'author')
    list_display = ['title', 'tag_list', 'created', 'modified', 'author'] + add_to_list_display()

    @staticmethod
    def tag_list(obj):
        return ", ".join(o.name for o in obj.tags.all().order_by('name'))


class CommentAdmin(ModelAdmin):
    list_display = ('text_preview', 'post_link', 'author', 'created_date')
    raw_id_fields = ('author',)

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
