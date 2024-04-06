from orders.models import Order, Payment, OrderItem
from rest_framework import serializers

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer()
    class Meta:
        model = Order
        fields = '__all__'

class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        
class OrderItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderItem
        fields = '__all__'