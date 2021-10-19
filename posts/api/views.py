# blog/posts/api/views.py
# Restframework modules
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
# My modules
from posts.models import Post
from posts.api.serializers import PostSerializer
from posts.api.permissions import IsAdminOrReadOnly

class PostApiViewSet(ModelViewSet):
    """
    Post Api View Serializer
    """
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published=True)
    lookup_field = 'slug'
    # Filter by category with django_filters
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'category__slug']
    # filterset_fields = ['category']
