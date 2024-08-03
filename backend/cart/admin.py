"""Admin-zone fo the cart app."""
from django.contrib import admin

from .models import CartItem


class CartItemInline(admin.TabularInline):
    """Cart item inline class."""

    model = CartItem
    readonly_fields = ('dish', 'quantity',)
    can_delete = False
    extra = 0
