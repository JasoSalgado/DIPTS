# blog/posts/models.py
# Django modules
from django.db import models
from django.db.models import SET_NULL
# My modules
from users.models import User
from categories.models import Category

class Post(models.Model):
    """
    Post model
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    thumbnail = models.ImageField(upload_to='posts/images/')
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True)
    
    def __str__(self):
        return self.title