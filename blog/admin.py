from django.contrib import admin

from .models import Post, Category, Tag
#from .models import Comment, EntryQuerySet, UserProfile

class EntryAdmin(admin.ModelAdmin):
    list_display = ("title", "pub_date")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ['pub_date']
    search_fields = ['title']

    
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Post, EntryAdmin)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(Comment)
admin.site.register(Tag, TagAdmin)
# admin.site.register(UserProfile)
