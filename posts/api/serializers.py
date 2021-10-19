# blog/posts/api/serializers.py
# Rest framework modules
from rest_framework import serializers
# My modules
from posts.models import Post
from users.api.serializers  import UserSerializer
from categories.api.serializers import CategorySerializer

class PostSerializer(serializers.ModelSerializer):
    """
    Post serializer
    """
    # To get all user information
    user = UserSerializer()
    # To get all category information
    category = CategorySerializer()

    class Meta:
        model = Post
        fields = ['title', 'content', 'slug', 
                    'thumbnail', 'created_at', 'published', 
                    'user', 'category']
        