# Generated by Django 4.1.7 on 2023-03-14 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_alter_basket_product_alter_order_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(related_name='products', to='webapp.product'),
        ),
    ]
