"""Serializers of api app."""
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

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
        slug_field='slug', many=True)

    class Meta:
        """Meta-data of the DishSerializer class."""

        model = Dish
        fields = ('name', 'category', 'price', 'image', 'is_on_main',
                  'is_new',)


class CompanyInfoSerializer(serializers.ModelSerializer):
    """Company info serializer."""

    class Meta:
        """Meta-data of the CompanyInfoSerialzer class."""

        model = CompanyInfo
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    """Order serializer."""

    dishes = serializers.ListField(required=True)

    class Meta:
        """Meta-data of the OrderSerialzer class."""

        model = Order
        fields = ('first_name', 'last_name', 'phone', 'email', 'address',
                  'delivery_address_lat', 'delivery_address_lng',
                  'dishes', 'delivery_type',)

    def create(self, validated_data):
        """Create Order object."""
        dishes = validated_data.pop('dishes')
        cart = Cart.objects.create()
        order = Order.objects.create(cart=cart, **validated_data)

        if not len(dishes):
            raise ValidationError('Поле dishes не должно быть пустым')
        for dish in dishes:
            if isinstance(dish, dict):
                try:
                    CartItem.objects.create(cart=cart, dish_id=dish['dish_id'],
                                            quantity=dish['quantity'])
                except KeyError:
                    raise ValidationError('Внутри объекта в поле dishes '
                                          'должны '
                                          'быть два ключа dish_id и quantity')
            else:
                raise ValidationError('Неправильно передана поле dishes. '
                                      'Он должен содержать объекты.')
        return order
