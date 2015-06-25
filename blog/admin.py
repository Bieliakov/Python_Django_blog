from django.contrib import admin

from .models import Post, Tag, Comment, EntryQuerySet


class EntryAdmin(admin.ModelAdmin):
    list_display = ("post_title", "post_pub_date")
    prepopulated_fields = {"post_slug": ("post_title",)}
    list_filter = ['post_pub_date']
    search_fields = ['post_title']

admin.site.register(Post, EntryAdmin)
admin.site.register(Tag)
admin.site.register(Comment)