from django.shortcuts import render
from django.views.generic import ListView
from product.filters import ProductFilter

from product.models import Product
# Create your views here.


class HomeView(ListView):
    template_name = 'product/home.html'
    queryset = Product.objects.all()
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['form'] = self.filterset.form
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs
