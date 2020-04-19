from django.contrib import admin
from .models import BlogPosts

class BlogPostsAdmin(admin.ModelAdmin):
    list_display = ["title", "date"]

admin.site.register(BlogPosts, BlogPostsAdmin)
