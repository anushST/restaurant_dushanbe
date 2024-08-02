"""Admin-zone fo the cart app."""
from .models import Cart, CartItem
from backend.admin_site import my_admin_site

my_admin_site.register(Cart)
my_admin_site.register(CartItem)
