"""Admin settings."""
from django.contrib.auth.admin import UserAdmin

from .models import User
from backend.admin_site import my_admin_site
from mail.models import EmailToGetConfirmation

my_admin_site.register(User, UserAdmin)
my_admin_site.register(EmailToGetConfirmation)
