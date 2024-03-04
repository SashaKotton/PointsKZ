from django.shortcuts import render, get_object_or_404
from products.models import Product
from orders.models import Order
from deliverers.models import Deliverer
from products.serializers import ProductSerializer
from orders.serializers import OrderSerializer
from deliverers.serializers import DelivererSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from authorization.permissions import IsSuperAdmin

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]
    

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

class DelivererList(generics.ListCreateAPIView):
    queryset = Deliverer.objects.all()
    serializer_class = DelivererSerializer
    permission_classes = [permissions.AllowAny]
    

class DelivererDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deliverer.objects.all()
    serializer_class = DelivererSerializer
    permission_classes = [permissions.IsAuthenticated]

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
