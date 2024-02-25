from django.urls import path, include
from api.views import ProductList, ProductDetail, OrderList, OrderDetail, DelivererList, DelivererDetail

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('product/<int:pk>', ProductDetail.as_view()),
    path('orders/', OrderList.as_view()),
    path('order/<int:pk>', OrderDetail.as_view()),
    path('deliverers/', DelivererList.as_view()),
    path('deliverer/<int:pk>', DelivererDetail.as_view()),
]