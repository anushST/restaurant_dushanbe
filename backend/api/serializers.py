"""Serializers of api app."""
from rest_framework import serializers

from cart.models import Cart, CartItem
from order.models import Order
from product.models import Category, Dish
from restaurant.models import CompanyInfo


class CategorySerializer(serializers.ModelSerializer):
    """Category serializer."""

    class Meta:
        """Meta-data of the CategorySerializer class."""

        model = Category
        fields = ('id', 'name', 'slug', 'is_on_main', 'image',)


class DishSerializer(serializers.ModelSerializer):
    """Dish serializer."""

    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug')

    class Meta:
        """Meta-data of the DishSerializer class."""

        model = Dish
        fields = ('name', 'category', 'price', 'image', 'is_on_main',
                  'is_new',)


class CartItemSerializer(serializers.ModelSerializer):
    """Cart item serializer."""

    class Meta:
        """Meta-data of the CartItemSerializer class."""

        model = CartItem
        fields = ('cart', 'dish', 'quantity',)


class CartSerializer(serializers.ModelSerializer):
    """Cart serializer."""

    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        """Meta-data of the CartSerializer class."""

        model = Cart
        fields = ('created_at', 'items')


class CompanyInfoSerializer(serializers.ModelSerializer):
    """Company info serializer."""

    class Meta:
        """Meta-data of the CompanyInfoSerialzer class."""

        model = CompanyInfo
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    """Order serializer."""

    cart = CartSerializer()

    class Meta:
        """Meta-data of the OrderSerialzer class."""

        model = Order
        fields = ('first_name', 'last_name', 'phone', 'address',
                  'delivery_address_lat', 'delivery_address_lng',
                  'cart', 'delivery_type',)
