# blog/posts/api/router.py
# Rest framework
from rest_framework.routers import DefaultRouter
# My modules
from posts.api.views import PostApiViewSet

router_posts = DefaultRouter()

router_posts.register(prefix="posts", basename="posts", viewset=PostApiViewSet)