from django.views.generic import DeleteView, View, TemplateView
from webapp.forms import OrderForm
from webapp.models import Product, Basket
from django.shortcuts import get_object_or_404, redirect, reverse
from django.db.models import Sum


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
        baskets = Basket.objects.all()
        for basket in baskets:
            ba = Basket.objects.aggregate(count=Sum(basket.qty))
            for k, v in ba.items():
                pass
        for p in product:
            pr = Product.objects.aggregate(count=Sum(p.price))
            for i, j in pr.items():
                pass
        context['total'] = v * j
        context['form'] = OrderForm
        return context


class BasketDelete(DeleteView):
    model = Basket

    def get_success_url(self):
        return reverse('basket')
