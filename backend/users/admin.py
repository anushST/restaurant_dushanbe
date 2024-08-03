"""Admin settings."""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from backend.admin_site import my_admin_site
from mail.models import EmailToGetConfirmation


class EmailToGetConfiramtionAdmin(admin.ModelAdmin):
    """EmailToGetConfirmation admin settings."""

    list_display = (
        'name',
        'email',
    )
    list_editable = (
        'email',
    )


class CustomUserAdmin(UserAdmin):
    """Custom Admin settings."""

    list_filter = []


my_admin_site.register(User, CustomUserAdmin)
my_admin_site.register(EmailToGetConfirmation, EmailToGetConfiramtionAdmin)
