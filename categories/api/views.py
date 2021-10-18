# blog/categories/api/views.py
# Rest framework modules
from rest_framework.viewsets import ModelViewSet
# from django_filters.rest_framework import DjangoFilterBackend

# My modules
from categories.models import Category
from categories.api.serializers import CategorySerializer
from categories.api.permissions import IsAdminOrReadOnly

class CategoryApiViewSet(ModelViewSet):
    """
    Category Api View Set
    """
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    # queryset = Category.objects.all()
    # It brings categories published True
    queryset = Category.objects.filter(published=True)
    lookup_field = 'slug'
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['published', 'title']
