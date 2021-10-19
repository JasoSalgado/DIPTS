# blog/comments/api/views.py
# Rest framework modules
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
# my modules
from comments.models import Comment
from comments.api.serializers import CommentSerializer
from comments.api.permissions import IsOwnerOrReadAndCreate

class CommentApiViewSet(ModelViewSet):
    """
    Comment api view set
    """
    permission_classes = [IsOwnerOrReadAndCreate]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering = ['-created_at']
    filterset_fields = ['post', 'post__slug']
