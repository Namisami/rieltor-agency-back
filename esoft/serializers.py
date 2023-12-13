from rest_framework import serializers
from .models import Client, Agent, ObjectType, Object, District, Offer, Demand, Deal

class ClientSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class AgentSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'

class ObjectTypeSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ObjectType
        fields = '__all__'

class ObjectSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Object
        fields = '__all__'

class DistrictSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = District
        fields = '__all__'

class OfferSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'

class DemandSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Demand
        fields = '__all__'

class DealSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Deal
        fields = '__all__'