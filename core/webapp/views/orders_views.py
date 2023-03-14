from django.views.generic import CreateView
from webapp.forms import OrderForm
from webapp.models import Order, Basket, Product
from django.shortcuts import redirect
from webapp.models.orderitem import OrderItem


class OrderViews(CreateView):
    template_name = 'basket.html'
    model = Order
    form_class = OrderForm

    def post(self, request, *args, **kwargs):
        product_in_basket = Basket.objects.all()
        products = Product.objects.all()
        form = OrderForm(data=request.POST)
        for basket in product_in_basket:
            for product in products:
                if not product:
                    return None
            basket.delete()
            OrderItem.objects.create(
                order=form.save(), product=basket.product, count=basket.qty
            )
        return redirect('index')
