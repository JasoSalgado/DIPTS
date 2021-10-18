# blog/users/admin.py
# Django modules
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# My modules
from users.models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass