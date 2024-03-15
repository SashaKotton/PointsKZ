from django.shortcuts import render, get_object_or_404
from products.models import Product
from orders.models import Order
from deliverers.models import Deliverer
from products.serializers import ProductSerializer
from orders.serializers import OrderSerializer
from deliverers.serializers import DelivererSerializer
from authorization.models import User
from authorization.serializers import UserProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework.viewsets import GenericViewSet 
from authorization.permissions import IsSuperAdmin
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class ProductList(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category','availability']
    search_fields = ['title',]
    ordering_fields = ['price',]
    ordering = ['price',]


class DelivererList(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Deliverer.objects.all()
    serializer_class = DelivererSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['delivery_company',]
    search_fields = ['name','surname','phone']
    ordering_fields = ['surname',]
    ordering = ['surname',]

    
class OrderList(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['payment', 'deliverer','payment_status','status','created_at','user_id',]
    search_fields = ['user_id','deliverer','status', 'payment_status']
    ordering_fields = ['created_at',]
    ordering = ['created_at',]

class UsersList(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['role', 'date_joined',]
    search_fields = ['username', 'first_name', 'email',]
    ordering_fields = ['date_joined',]
    ordering = ['date_joined']
    

# class ProductList(APIView):

#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many = True)
#         return Response(serializer.data)        

#     def post(self, request):
#         serializer = ProductSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class ProductDetail(APIView):

#     def get(self, request, pk):
#         product = get_object_or_404(Product.objects.all(), pk=pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = ProductSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def put(self, request, pk):
#         product = get_object_or_404(Product.objects.all(), pk=pk)
#         serializer = ProductSerializer(product, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_200_OK)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         product = get_object_or_404(Product.objects.all(), pk=pk)
#         product.delete()
#         return Response(status=status.HTTP_404_NOT_FOUND)
