from django.shortcuts import render, get_object_or_404
from products.models import Product, Category
from orders.models import Order, Payment, OrderItem
from deliverers.models import Deliverer, DeliveryCompany
from products.serializers import ProductSerializer, ProductCreateSerializer, CategorySerializer
from orders.serializers import OrderSerializer, OrderItemSerializer, PaymentSerializer
from deliverers.serializers import DelivererSerializer, DelivererCompanySerializer
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
from authorization.permissions import IsBasic, IsCourier, IsSuperAdmin
import requests

#Добавить стороннее API, Добавить удаление пользователя, добавить местоположение пользователя

class ProductList(GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Product.objects.all()
    permission_classes_by_action = {
        'list':[permissions.AllowAny],
        'create':[permissions.IsAuthenticated & IsSuperAdmin],
        'retrive':[permissions.AllowAny],
        'update':[permissions.IsAuthenticated & IsSuperAdmin],
        'destroy':[permissions.IsAuthenticated & IsSuperAdmin],
    }
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category','availability']
    search_fields = ['title',]
    ordering_fields = ['price',]
    ordering = ['price',]

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return []
        
    def get_serializer_class(self):
        if self.action == 'list':
            return ProductSerializer
        if self.action == 'create':
            return ProductCreateSerializer
        if self.action == 'retrive':
            return ProductSerializer
        if self.action == 'update':
            return ProductSerializer
        if self.action == 'destroy':
            return ProductCreateSerializer


class DelivererList(GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Deliverer.objects.all()
    serializer_class = DelivererSerializer
    permission_classes_by_action = {
        'list':[permissions.AllowAny],
        'create':[permissions.IsAuthenticated & IsSuperAdmin],
        'retrive':[permissions.AllowAny],
        'update':[permissions.IsAuthenticated & IsSuperAdmin],
        'destroy':[permissions.IsAuthenticated & IsSuperAdmin],
    }
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['delivery_company',]
    search_fields = ['name','surname','phone']
    ordering_fields = ['surname',]
    ordering = ['surname',]

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return []

    
class OrderList(GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes_by_action = {
        'list':[permissions.AllowAny],
        'create':[permissions.IsAuthenticated & IsSuperAdmin],
        'retrive':[permissions.AllowAny],
        'update':[permissions.IsAuthenticated & IsSuperAdmin],
        'destroy':[permissions.IsAuthenticated & IsSuperAdmin],
    }
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['payment', 'deliverer','payment_status','status','created_at','user_id',]
    search_fields = ['user_id','deliverer','status', 'payment_status']
    ordering_fields = ['created_at',]
    ordering = ['created_at',]

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return []

class UsersList(GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes_by_action = {
        'list':[permissions.AllowAny],
        'create':[permissions.IsAuthenticated & IsSuperAdmin],
        'retrive':[permissions.AllowAny],
        'update':[permissions.IsAuthenticated & IsSuperAdmin],
        'destroy':[permissions.IsAuthenticated & IsSuperAdmin],
    }
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['role', 'date_joined',]
    search_fields = ['username', 'first_name', 'email',]
    ordering_fields = ['date_joined',]
    ordering = ['date_joined']

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return []
        
class CategoryList(GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes_by_action = {
        'list':[permissions.AllowAny],
        'create':[permissions.IsAuthenticated & IsSuperAdmin],
        'retrive':[permissions.AllowAny],
        'update':[permissions.IsAuthenticated & IsSuperAdmin],
        'destroy':[permissions.IsAuthenticated & IsSuperAdmin],
    }
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title',]
    search_fields = ['title', ]
    ordering_fields = ['title',]
    ordering = ['title',]

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return []
        
class PaymentList(GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes_by_action = {
        'list':[permissions.AllowAny],
        'create':[permissions.IsAuthenticated & IsSuperAdmin],
        'retrive':[permissions.AllowAny],
        'update':[permissions.IsAuthenticated & IsSuperAdmin],
        'destroy':[permissions.IsAuthenticated & IsSuperAdmin],
    }
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title','total_price',]
    search_fields = ['title','total_price', ]
    ordering_fields = ['title','total_price',]
    ordering = ['title',]

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return []
    
class OrderItemList(GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes_by_action = {
        'list':[permissions.AllowAny],
        'create':[permissions.IsAuthenticated & IsSuperAdmin],
        'retrive':[permissions.AllowAny],
        'update':[permissions.IsAuthenticated & IsSuperAdmin],
        'destroy':[permissions.IsAuthenticated & IsSuperAdmin],
    }
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['order',]
    search_fields = ['product','order', ]
    ordering_fields = ['quantity','amount',]
    ordering = ['quantity',]

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return []
        
class DeliveryCompanyList(GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = DeliveryCompany.objects.all()
    serializer_class = DelivererCompanySerializer
    permission_classes_by_action = {
        'list':[permissions.AllowAny],
        'create':[permissions.IsAuthenticated & IsSuperAdmin],
        'retrive':[permissions.AllowAny],
        'update':[permissions.IsAuthenticated & IsSuperAdmin],
        'destroy':[permissions.IsAuthenticated & IsSuperAdmin],
    }
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title','phone']
    search_fields = ['title','phone', ]
    ordering_fields = ['title','phone',]
    ordering = ['title',]

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return []
        
class UserLocationView(GenericViewSet):
    def get_location(self, request):
        

        url = "https://ipinfo.io/json"

        payload = {}
        files={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload, files=files)

        return Response(data=response.json(), status=status.HTTP_200_OK)

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
