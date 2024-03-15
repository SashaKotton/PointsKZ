from django.urls import path, include
from api.views import ProductList, DelivererList, OrderList, UsersList
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products',ProductList, basename='products')
router.register('deliverers', DelivererList, basename='deliverer')
router.register('orders', OrderList, basename='order')
router.register('users', UsersList, basename='users')

urlpatterns = [
    # path('', include(router.urls)),

]
urlpatterns += router.urls