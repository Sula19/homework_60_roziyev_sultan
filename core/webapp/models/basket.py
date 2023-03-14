from django.db import models


class Basket(models.Model):
    product = models.ForeignKey(
        to='webapp.Product',
        related_name='product',
        on_delete=models.CASCADE,
        verbose_name='Продукт'
    )
    qty = models.IntegerField(
        verbose_name='Количество',
        default=1
    )

    def __str__(self):
        return f'{self.product} - {self.qty}'

    def summary(self):
        return f'{self.product.price * self.qty}'

