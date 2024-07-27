"""All project's models."""
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """User model."""

    class Meta():
        """Meta-data of the Cart class."""

        verbose_name = 'персонал'
        verbose_name_plural = 'Перснонал'
