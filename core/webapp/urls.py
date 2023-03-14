from django.urls import path
from webapp.views.products_views import IndexViews, AddViews, DetailViews, UpdateViews, DeleteViews
from webapp.views.baskets_views import IndexBasket, AddToBasket, BasketDelete
from webapp.views.orders_views import OrderViews


urlpatterns = [
    path('', IndexViews.as_view(), name='index'),
    path('basket', IndexBasket.as_view(), name='basket'),
    path('basket/order/', OrderViews.as_view(), name='order'),
    path('product/add', AddViews.as_view(), name='add_product'),
    path('product/<int:pk>', DetailViews.as_view(), name='detail_product'),
    path('product/update/<int:pk>', UpdateViews.as_view(), name='update_product'),
    path('product/delete/<int:pk>', DeleteViews.as_view(), name='delete_product'),
    path('product/<int:pk>/add_basket', AddToBasket.as_view(), name='add_basket'),
    path('basket/<int:pk>/delete', BasketDelete.as_view(), name='delete_basket'),
]
