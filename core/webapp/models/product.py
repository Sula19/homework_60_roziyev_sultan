from django.db import models
from django.db.models import TextChoices


class ProductChoice(TextChoices):
    PC = 'PC', 'ПК'
    NOTEBOOK = 'NoteBook', 'Ноутбук'
    SMARTPHONE = 'SmartPhone', 'Смартфоны'


class Product(models.Model):
    name = models.CharField(
        max_length=60,
        null=False,
        blank=False,
        verbose_name='Наименование'
    )
    description = models.TextField(
        max_length=1700,
        blank=True,
        verbose_name='Описание'
    )
    category = models.CharField(
        choices=ProductChoice.choices,
        default='Other',
        max_length=70,
        verbose_name='Категория'
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False,
        verbose_name='Цена'
    )
    remainder = models.IntegerField(
        verbose_name='Остаток'
    )
    img = models.CharField(
        max_length=400,
        null=False,
        blank=False,
        verbose_name='Фото'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время создания'
    )

    def __str__(self):
        return f'{self.category} - {self.name}'
