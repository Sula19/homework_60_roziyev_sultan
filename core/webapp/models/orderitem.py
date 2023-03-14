from django.db import models


class OrderItem(models.Model):
    order = models.ForeignKey(to='webapp.Order', on_delete=models.PROTECT)
    product = models.ForeignKey(to='webapp.Product', on_delete=models.PROTECT)
    count = models.IntegerField(verbose_name='Количество')
