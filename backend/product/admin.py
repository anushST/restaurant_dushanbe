"""Admin-zone of the product app."""
from django.contrib import admin

from .models import Category, Dish

admin.site.register((Category, Dish))
