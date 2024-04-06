from django.urls import path, include
from api.views import ProductList, DelivererList, JokeView, OrderList, UsersList, DeliveryCompanyList, PaymentList, OrderItemList, CategoryList, UserLocationView
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
    path('location/', UserLocationView.as_view({'get':'get_location'})),
    path('joke/', JokeView.as_view({'get':'joke'})),
]
urlpatterns += router.urls