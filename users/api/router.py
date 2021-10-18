# blog/users/api/router.py
# Rest framework modules
# Rest framework modules
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# Django modules
from django.urls import path

# My modules
from users.api.views import RegisterView, UserView

urlpatterns = [
    path('auth/register', RegisterView.as_view()),
    path('auth/login', TokenObtainPairView.as_view()),
    path('auth/token/refresh', TokenRefreshView.as_view()),
    path('auth/me', UserView.as_view()),
]