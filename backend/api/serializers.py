"""Serializers of api app."""
from django.shortcuts import get_object_or_404
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

    categories = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug', many=True)

    class Meta:
        """Meta-data of the DishSerializer class."""

        model = Dish
        fields = ('id', 'name', 'description', 'categories', 'price',
                  'old_price', 'weight', 'image', 'is_on_main', 'is_new',)


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

    def validate_dishes(self, value):
        """Validate dish field."""
        if not len(value):
            raise ValidationError('Поле dishes не должно быть пустым')

        for dish in value:
            if isinstance(dish, dict):
                if 'dish_id' not in dish and 'quantity' not in dish:
                    raise ValidationError('Внутри объекта в поле dishes '
                                          'должны '
                                          'быть два ключа dish_id и quantity')
            else:
                raise ValidationError('Неправильно передана поле dishes. '
                                      'Он должен содержать объекты.')
        return value

    def validate(self, data):
        """Validate data."""
        super().validate(data)
        delivery_type = data.get('delivery_type')
        address = data.get('address')
        if delivery_type == 'courier' and (not address or address == ''):
            raise ValidationError('Нужен адрес доставки.')
        return data

    def count_total_price_and_check_dish_values(
            self, dishes):
        """Count total price and check the dish values."""
        total_price = 0

        for dish in dishes:
            dish_object = get_object_or_404(Dish, pk=dish['dish_id'])
            try:
                quantity = int(dish['quantity'])
            except ValueError:
                raise ValidationError('Значение ключа quantity поля '
                                      'dishes должно быть int.')
            total_price += dish_object.price * quantity
        return total_price

    def create(self, validated_data):
        """Create Order object."""
        dishes = validated_data.pop('dishes')
        cart = Cart.objects.create()
        total_price = self.count_total_price_and_check_dish_values(dishes)
        order = Order.objects.create(cart=cart, total_price=total_price,
                                     **validated_data)

        for dish in dishes:
            CartItem.objects.create(cart=cart, dish_id=dish['dish_id'],
                                    quantity=dish['quantity'])
        return order
