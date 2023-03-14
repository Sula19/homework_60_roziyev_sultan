from django.views.generic import DeleteView, View, TemplateView
from webapp.forms import OrderForm
from webapp.models import Product, Basket
from django.shortcuts import get_object_or_404, redirect, reverse
from django.db.models import Sum, FloatField, IntegerField


class AddToBasket(View):

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs.get('pk'))
        baskets = Basket.objects.filter(product=product.pk)
        if baskets:
            for basket in baskets:
                if basket.qty >= product.remainder:
                    pass
                else:
                    basket.qty += 1
                    basket.save()
                return redirect('index')
        if product not in baskets and product.remainder > 0:
            Basket.objects.create(
                product=product,
                qty=1
            )

        else:
            pass
        return redirect('index')


class IndexBasket(TemplateView):
    template_name = 'basket.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['baskets'] = Basket.objects.all()
        product = Product.objects.all()
        for p in product:
            context['total'] = Product.objects.aggregate(count=Sum(p.price))
        context['form'] = OrderForm
        return context


class BasketDelete(DeleteView):
    model = Basket

    def get_success_url(self):
        return reverse('basket')
