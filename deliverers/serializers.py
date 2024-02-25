from deliverers.models import Deliverer, DeliveryCompany
from rest_framework import serializers

class DelivererCompanySerializer(serializers.ModelSerializer):

    class Meta: 
        model = DeliveryCompany
        fields = '__all__'

class DelivererSerializer(serializers.ModelSerializer):
    delivery_company = DelivererCompanySerializer()
    class Meta:
        model = Deliverer
        fields = '__all__'