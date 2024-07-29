"""Models of the cart app."""
from django.db import models

from product.models import Dish


class Cart(models.Model):
    """Cart model."""

    created_at = models.DateTimeField('Время создания', auto_now_add=True)

    def __str__(self):
        """Return the string when calling str() method on this obj."""
        return f'Корзина {self.id}'

    class Meta():
        """Meta-data of the Cart class."""

        verbose_name = 'корзина'
        verbose_name_plural = 'Корзины'
        ordering = ('id',)


class CartItem(models.Model):
    """Cart Item model."""

    cart = models.ForeignKey(Cart, related_name='items',
                             on_delete=models.CASCADE,
                             verbose_name='Корзина')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE,
                             verbose_name='Блюдо')
    quantity = models.PositiveIntegerField('Количество', default=1)

    def __str__(self):
        """Return the string when calling str() method on this obj."""
        return f'{self.quantity} x {self.dish.name}'

    class Meta:
        """Meta-data of the CartItem class."""

        verbose_name = 'товар корзины'
        verbose_name_plural = 'Товары корзины'
