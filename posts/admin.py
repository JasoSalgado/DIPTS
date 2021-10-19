# blog/posts/admin.py
# Django modules
from django.contrib import admin
# My modules
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Register post admin
    """
    list_display = ['title', 'user', 'created_at', 'published']


