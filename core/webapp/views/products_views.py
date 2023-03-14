from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from webapp.models import Product
from webapp.forms import ProductForm, SearchForm
from django.utils.http import urlencode
from django.db.models import Q


class IndexViews(ListView):
    template_name = 'index.html'
    context_object_name = 'products'
    model = Product
    paginate_by = 5
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(name__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class AddViews(CreateView):
    template_name = 'add_product.html'
    form_class = ProductForm
    model = Product
    success_url = '/'


class UpdateViews(UpdateView):
    template_name = 'update_product.html'
    form_class = ProductForm
    model = Product
    success_url = '/'


class DeleteViews(DeleteView):
    template_name = 'delete_product.html'
    context_object_name = 'product'
    model = Product
    success_url = '/'


class DetailViews(DetailView):
    template_name = 'detail_product.html'
    model = Product
