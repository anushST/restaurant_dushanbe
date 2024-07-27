"""Views of the api app."""
from rest_framework import viewsets

from .serializers import (CartSerializer, CategorySerializer,
                          CompanyInfoSerializer, DishSerializer,
                          OrderSerializer)
from cart.models import Cart
from order.models import Order
from product.models import Category, Dish
from restaurant.models import CompanyInfo


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """Category viewset."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class CompanyInfoViewSet(viewsets.ReadOnlyModelViewSet):
    """Comapny info viewset."""

    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoSerializer


class DishViewSet(viewsets.ReadOnlyModelViewSet):
    """Dish viewset."""

    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class CartViewSet(viewsets.ModelViewSet):
    """Cart viewset."""

    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """Order viewset."""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
