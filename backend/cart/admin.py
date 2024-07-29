"""Admin zone of admin app."""
from django.contrib import admin

from .models import Cart, CartItem


class ReadOnlyAdmin(admin.ModelAdmin):
    """ModelAdmin which is only ReadOnly."""

    def has_add_permission(self, request):
        """Allow adding."""
        return False

    def has_change_permission(self, request, obj=None):
        """Allow changing."""
        return False

    def has_delete_permission(self, request, obj=None):
        """Allow deleting."""
        return False

    def get_actions(self, request):
        """Return all actions."""
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


class CartItemInline(admin.TabularInline):
    """Represent CartItem Inline."""

    model = CartItem
    extra = 0
    readonly_fields = ('cart', 'dish', 'quantity')
    can_delete = False

    def has_add_permission(self, request, obj=None):
        """Allow Add."""
        return False

    def has_change_permission(self, request, obj=None):
        """Allow edit."""
        return False


class CartAdmin(ReadOnlyAdmin):
    """Cart Admin."""

    inlines = [CartItemInline]


admin.site.register(Cart, CartAdmin)
