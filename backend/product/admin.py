"""Admin-zone of the product app."""
from .models import Category, Dish
from backend.admin_site import my_admin_site

my_admin_site.register(Category)
my_admin_site.register(Dish)
