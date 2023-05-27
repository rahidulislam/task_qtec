import django_filters

from .models import Category, Brand, Product

class ProductFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()
    
    class Meta:
        model=Product
        fields = ['category', 'brand','price', ]

    
