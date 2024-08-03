"""Models of the cart app."""
from django.db import models

from product.models import Dish
from order.models import Order


class CartItem(models.Model):
    """Cart Item model."""

    dish = models.ForeignKey(Dish, on_delete=models.CASCADE,
                             verbose_name='Блюдо')
    quantity = models.PositiveIntegerField('Количество', default=1)
    order = models.ForeignKey(Order, verbose_name='Заказ',
                              on_delete=models.CASCADE,
                              related_name='cart_item_order')

    def __str__(self):
        """Return the string when calling str() method on this obj."""
        return f'{self.dish.name}'

    class Meta:
        """Meta-data of the CartItem class."""

        verbose_name = 'товар корзины'
        verbose_name_plural = 'Товары корзины'
