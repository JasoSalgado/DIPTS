# blog/comments/api/serializers.py
# Rest framework modules
from rest_framework import serializers
# My modules
from comments.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    """
    Comment serializer
    """
    class Meta:
        model = Comment
        fields = ['content', 'created_at', 'user', 'post']
