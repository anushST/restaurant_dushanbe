"""Admin-zone of the restaurant app."""
from django.contrib import admin

from .models import CompanyInfo
from backend.admin_site import my_admin_site


class CompanyInfoAdmin(admin.ModelAdmin):
    """Admin settings of the CompanyInfo model."""

    def has_add_permission(self, request):
        """Can not add objects."""
        return False

    def has_delete_permission(self, request, obj=None):
        """Can not delete objects."""
        return False


my_admin_site.register(CompanyInfo, CompanyInfoAdmin)
