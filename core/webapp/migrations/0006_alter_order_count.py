# Generated by Django 4.1.7 on 2023-03-13 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_remove_basket_is_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='count',
            field=models.IntegerField(default=1, verbose_name='Количество'),
        ),
    ]
