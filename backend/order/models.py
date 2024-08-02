"""Models of the order app."""
from django.core.exceptions import ValidationError
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
    last_name = models.CharField('Фамилия', max_length=100,
                                 null=True, blank=True)
    phone = PhoneNumberField(verbose_name='Телефон')
    email = models.EmailField('Email')
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
    total_price = models.DecimalField('Общая цена', max_digits=6,
                                      decimal_places=2)
    is_accepted = models.BooleanField('Прнинято?', default=False)
    is_delivered = models.BooleanField('Доставлено?', default=False)
    dishes = models.TextField('Для работы сериализатора', editable=False)

    def clean(self) -> None:
        """Validate fields."""
        super().clean()
        if self.delivery_type == 'courier' and not self.address:
            raise ValidationError('Нужен адрес доставки.')

    def __str__(self):
        """Return the string when calling str() method on this obj."""
        return (f'{self.first_name} '
                f'{self.last_name if self.last_name else ""}')

    class Meta():
        """Meta-data of the Order class."""

        verbose_name = 'заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('id',)
