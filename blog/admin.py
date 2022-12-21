from django.contrib import admin
from .models import Blog, Author, Category
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_filter = [ # Whic fields to use for filtering
        "author",
        "title",
        "category"
    ]
    list_display = [ # Which fields to show in the table
        "title",
        "author"
    ]

admin.site.register(Blog, BlogAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "country"
    ]
    list_filter = [
        "country"
    ]
admin.site.register(Author, AuthorAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "code"
    ]

admin.site.register(Category, CategoryAdmin)