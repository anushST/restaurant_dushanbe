"""Models of the product app."""
from django.db import models


class Category(models.Model):
    """Category model."""

    name = models.CharField('Название категории', max_length=100)
    slug = models.SlugField(
        'Идентификатор', unique=True,
        help_text=('Идентификатор должен быть позож на '
                   'имя категории, но на английском языке.'))
    is_on_main = models.BooleanField('Добавить на главную страницу?',
                                     default=False)
    image = models.ImageField('Фото', upload_to='categories_photos/')

    def __str__(self):
        """Return the string when calling str() method on this obj."""
        return self.name

    class Meta():
        """Meta-data of the Category class."""

        verbose_name = 'категория'
        verbose_name_plural = 'Категории'
        ordering = ('id',)


class Dish(models.Model):
    """Dish model."""

    name = models.CharField('Названия блюда', max_length=100)
    description = models.TextField('Описание блюда', max_length=1024*6)
    categories = models.ManyToManyField(Category, related_name='dishes',
                                        verbose_name='Категория блюда')
    price = models.DecimalField('Цена', max_digits=6, decimal_places=2)
    weight = models.DecimalField('Вес в граммах', max_digits=6,
                                 decimal_places=2, null=True, blank=True)
    old_price = models.DecimalField('Цена без скидки', max_digits=6,
                                    decimal_places=2,
                                    null=True, blank=True,
                                    help_text='Ставтьте значение в этом поле только в том случае если хотите чтобы был эффект скидки. Т.е эта цена на сайте будет зачёркнута. Если не хотите такого, просто оставьте это поле пустым.')  # noqa: E501
    image = models.ImageField('Фото', upload_to='dishes_photos/')
    is_on_main = models.BooleanField('Добавить на главную страницу?',
                                     default=False)
    is_new = models.BooleanField('Добавить в раздел новые?', default=False)

    def __str__(self):
        """Return the string when calling str() method on this obj."""
        return f'{self.name} ({self.price})'

    class Meta():
        """Meta-data of the Cart class."""

        verbose_name = 'блюдо'
        verbose_name_plural = 'Блюда'
        ordering = ('id',)
