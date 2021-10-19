# blog/comments/models.py
# Django modules
from django.db import models
from django.db.models import CASCADE
# my modules
from users.models import User
from posts.models import Post

class Comment(models.Model):
    """
    Comments model
    """
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)


