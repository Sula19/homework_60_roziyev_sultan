from django.db import models


class Order(models.Model):
    product = models.ManyToManyField(
        'webapp.Product',
        related_name='products',
        through='webapp.OrderItem'
    )
    user = models.CharField(
        max_length=65,
        null=False,
        blank=False,
        verbose_name='Имя пользователя'
    )
    phone = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        verbose_name='Телефон'
    )
    address = models.CharField(
        max_length=80,
        null=False,
        blank=False,
        verbose_name='Адрес'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время создания'
    )

    def __str__(self):
        return f'{self.user} - {self.phone} - {self.address}'
