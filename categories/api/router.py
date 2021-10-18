# blog/categories/api/router.py
# Rest framework modules
from rest_framework.routers import DefaultRouter

# My modules
from categories.api.views import CategoryApiViewSet

router_categories = DefaultRouter()

router_categories.register(prefix='categories', 
                            basename='categories', 
                            viewset=CategoryApiViewSet)