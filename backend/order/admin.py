"""Admin-zone of the order app."""
from django.contrib import admin

from .models import Order
from backend.admin_site import my_admin_site


class OrderAdmin(admin.ModelAdmin):
    """Admin settings class for order model."""

    list_display = (
        'first_name',
        'last_name',
        'phone',
        'delivery_type',
        'address',
        'is_accepted',
        'is_delivered',
    )
    list_editable = (
        'is_accepted',
        'is_delivered',
    )


my_admin_site.register(Order, OrderAdmin)
