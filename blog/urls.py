# blog/urls.py
# Django modules
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

# My API modules
from categories.api.router import router_categories
from posts.api.router import router_posts
from comments.api.router import router_comments

"""
API documentation config
"""
schema_view = get_schema_view (
    openapi.Info(
        title="DIPTS API",
        default_version="v1",
        description="DIPTS API Documentation",
        terms_of_service="", #Add terms of the service
        contact=openapi.Contact(email=""),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path('redocs/', schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path('api/', include('users.api.router')),
    path('api/', include(router_categories.urls)),
    path('api/', include(router_posts.urls)),
    path('api/', include(router_comments.urls)),
]
