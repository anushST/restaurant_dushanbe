"""Models of the restaurant app."""
from django.db import models


class CompanyInfo(models.Model):
    """Company information model."""

    address = models.TextField('Адрес', max_length=512)
    working_hours = models.TextField('Часы работы', max_length=512)
    phones = models.TextField('Телефонные номера', max_length=512)
    delivery_cost = models.TextField('Политика доставки', max_length=512,
                                     null=True, blank=True)
    delivery_time = models.TextField('Время доставки', max_length=512,
                                     null=True, blank=True)
    payment_methods = models.TextField('Способы оплаты', max_length=512,
                                       null=True, blank=True)
    whatsapp_link = models.URLField('Whatsapp ссылка', null=True,
                                    blank=True)
    telegram_link = models.URLField('Telegram ссылка', null=True,
                                    blank=True)
    instagram_link = models.URLField('Instagram ссылка', null=True,
                                     blank=True)

    def __str__(self):
        """Return the string when calling str() method on this obj."""
        return 'Информация о компании.'

    class Meta():
        """Meta-data of the Cart class."""

        verbose_name = 'информация о компании'
        verbose_name_plural = 'Информация о компании'
        ordering = ('id',)
