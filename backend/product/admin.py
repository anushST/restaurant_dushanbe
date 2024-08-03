"""Admin-zone of the product app."""
from django.contrib import admin

from .models import Category, Dish
from backend.admin_site import my_admin_site


class CategoryAdmin(admin.ModelAdmin):
    """Category Admin settings."""

    list_display = (
        'name',
        'slug',
        'is_on_main'
    )
    list_editable = (
        'slug',
        'is_on_main',
    )


class DishAdmin(admin.ModelAdmin):
    """Dish Admin settings."""

    filter_horizontal = ('categories',)
    list_display = (
        'name',
        'price',
        'weight',
        'is_new',
        'is_on_main',
    )
    list_editable = (
        'price',
        'weight',
        'is_new',
        'is_on_main',
    )


my_admin_site.register(Category, CategoryAdmin)
my_admin_site.register(Dish, DishAdmin)
