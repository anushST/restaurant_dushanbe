"""Models of the restaurant app."""
from django.db import models


class CompanyInfo(models.Model):
    """Company information model."""

    address = models.CharField('Адрес', max_length=255)
    working_hours = models.CharField('Часы работы', max_length=255)
    phone = models.CharField('Телефонные номера', max_length=64)
    delivery_cost = models.CharField('Политика доставки', max_length=512)
    delivery_time = models.CharField('Время доставки', max_length=100)
    payment_methods = models.CharField('Способы оплаты', max_length=255)
    whatsapp_link = models.URLField('Whatsapp ссылка')
    telegram_link = models.URLField('Telegram ссылка')
    instagram_link = models.URLField('Instagram ссылка')

    class Meta():
        """Meta-data of the Cart class."""

        verbose_name = 'информация о компании'
        verbose_name_plural = 'Информация о компании'
