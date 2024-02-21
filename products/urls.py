from django.urls import path, include
from products.views import product_list, product_detail, add_new_product, edit_product

urlpatterns = [
    path('', product_list, name='product_list'),
    path('detail/<int:pk>', product_detail, name='product_detail'),
    path('new/', add_new_product, name='add_new_product'),
    path('edit/<int:pk>', edit_product, name = 'edit_product')
]