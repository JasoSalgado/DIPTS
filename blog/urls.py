# blog/urls.py
# Django modules
from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

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
]
