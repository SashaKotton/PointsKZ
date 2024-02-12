from django.urls import path, include
from products.views import product_list

urlpatterns = [
    path('', product_list, name='product_list')
]