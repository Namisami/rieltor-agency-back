from rest_framework import serializers
from .models import Client, Agent, Types, Object, District, Offer, Need, Deal

class ClientSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class AgentSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'

class TypesSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Types
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

class NeedSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Need
        fields = '__all__'

class DealSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Deal
        fields = '__all__'