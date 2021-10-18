# blog/users/models.py
# Django modules
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Override user model
    """
    # To login will be with email
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

