from django import forms
from .models import Product, Order, Basket


class ProductForm(forms.ModelForm):
    remainder = forms.IntegerField(min_value=0, required=True, label='Остаток')

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'remainder', 'category', 'img']
        labels = {
            'name': 'Наименование',
            'description': 'Описание',
            'price': 'Цена',
            'remainder': 'Остаток',
            'category': 'Категория',
            'img': 'Фото'
        }


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['user', 'phone', 'address']
        labels = {
            'user': 'Имя',
            'phone': 'Телефон',
            'address': 'Адрес'
        }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=80, required=False, label='Найти')
