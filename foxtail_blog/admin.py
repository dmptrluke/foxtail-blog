from django.contrib import admin
from django.contrib.admin import ModelAdmin

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
            'classes': ('collapse',),
            'fields': ('slug',),
        }),
    )

    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('created', 'tags', 'author')
    list_display = ('title', 'tag_list', 'created', 'modified', 'author')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


class CommentAdmin(ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
