# blog/categories/admin.py
# Django modules
from django.contrib import admin

# My modules
from categories.models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Category admin
    """
    list_display = ['title', 'published']