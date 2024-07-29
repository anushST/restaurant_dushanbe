"""Admin-zone of the order app."""
from django.contrib import admin
from .models import Order

admin.site.register(Order)
