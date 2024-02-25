from orders.models import Order, Payment
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