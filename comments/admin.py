# blog/comments/admin.py
from django.contrib import admin

# My modules
from comments.models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Comments admin
    """
    #serializer =
    list_display = ['content', 'user', 'post', 'created_at']
