from django.urls import path, include
from products.views import product_list, product_detail

urlpatterns = [
    path('', product_list, name='product_list'),
    path('detail/<int:pk>', product_detail, name='product_detail')
]