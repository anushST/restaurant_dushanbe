"""Models of the mail app."""
from django.db import models


class EmailToGetConfirmation(models.Model):
    """Emails which will sent confirmation code."""

    name = models.CharField('Имя', max_length=256)
    email = models.EmailField('Email')

    def __str__(self):
        """Return the string when calling str() method on this obj."""
        return f'{self.name}'

    class Meta:
        """Meta-data of the EmailToGetConfirmation class."""

        verbose_name = 'email для получения подтверждения заказа.'
        verbose_name_plural = 'Email-ы для получения подтверждения заказа.'
        ordering = ('id',)
