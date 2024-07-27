"""Models of the order app."""
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from cart.models import Cart


class Order(models.Model):
    """Order model."""

    DELIVERY_CHOICES = [
        ('courier', 'Курьер'),
        ('pickup', 'Самовызов'),
    ]
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    phone = PhoneNumberField(verbose_name='Телефон')
    address = models.CharField('Адрес доставки', max_length=256,
                               null=True, blank=True)
    delivery_address_lat = models.DecimalField('Ширина', max_digits=9,
                                               decimal_places=6,
                                               null=True, blank=True)
    delivery_address_lng = models.DecimalField('Долгота', max_digits=9,
                                               decimal_places=6,
                                               null=True, blank=True)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE,
                                verbose_name='Корзина')
    delivery_type = models.CharField('Тип заказа', max_length=10,
                                     choices=DELIVERY_CHOICES)

    class Meta():
        """Meta-data of the Order class."""

        verbose_name = 'заказ'
        verbose_name_plural = 'Заказаы'
