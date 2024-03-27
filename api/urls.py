from django.urls import path, include
from api.views import ProductList, DelivererList, OrderList, UsersList, DeliveryCompanyList, PaymentList, OrderItemList, CategoryList
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products',ProductList, basename='products')
router.register('category', CategoryList, basename='category')
router.register('deliverers', DelivererList, basename='deliverer')
router.register('orders', OrderList, basename='order')
router.register('users', UsersList, basename='users')
router.register('deliverycompany', DeliveryCompanyList, basename='deliverycompany')
router.register('payment', PaymentList, basename='payment')
router.register('orderitem', OrderItemList, basename='orderitem')



urlpatterns = [
    # path('', include(router.urls)),

]
urlpatterns += router.urls