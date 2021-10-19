# blog/comments/api/router.py
# Rest framework modules
from rest_framework.routers import DefaultRouter

# My modules
from comments.api.views import CommentApiViewSet

router_comments = DefaultRouter()

router_comments.register(prefix="comments", basename="comments", viewset=CommentApiViewSet)