"""Admin-zone of the order app."""
from django.contrib import admin

from .models import Order
from backend.admin_site import my_admin_site
from cart.admin import CartItemInline


class OrderAdmin(admin.ModelAdmin):
    """Admin settings class for order model."""

    inlines = (CartItemInline,)

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
    empty_value_display = 'Не задано'
    readonly_fields = (
        'first_name',
        'last_name',
        'phone',
        'email',
        'address',
        'delivery_type',
        'total_price',
    )

    def has_add_permission(self, request):
        """Can not add objects."""
        return False


my_admin_site.register(Order, OrderAdmin)
