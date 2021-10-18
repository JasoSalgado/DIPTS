# blog/categories/api/serializers.py
# Rest framework modules
from rest_framework import serializers

# My modules
from categories.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug', 'published']