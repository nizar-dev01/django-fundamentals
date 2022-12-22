from django.contrib import admin
# Register your models here.

from .models import Author, Tag, Post

class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "email"
    ]

class TagAdmin(admin.ModelAdmin):
    list_display = [
        "caption"
    ]

class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "author",
        "slug"
    ]
    list_filter = [
        "tags"
    ]

admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)