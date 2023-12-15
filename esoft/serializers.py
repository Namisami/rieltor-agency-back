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
    def __init__(self, *args, **kwargs):
        super(ObjectSerializers, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT' or request.method == 'PATCH'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

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
    def __init__(self, *args, **kwargs):
        super(DemandSerializers, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT' or request.method == 'PATCH'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1
            
    class Meta:
        model = Demand
        fields = ['id', 'url', 'address_city', 'address_street', 'address_house', 'address_number', 'min_price', 'max_price', 'agent', 'client', 'type', 'min_area', 'max_area', 'min_rooms', 'max_rooms', 'min_floor', 'max_floor', 'min_floors', 'max_floors', 'active']

class DealSerializers(serializers.HyperlinkedModelSerializer):
    def __init__(self, *args, **kwargs):
        super(DealSerializers, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT' or request.method == 'PATCH'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 2
            
    class Meta:
        model = Deal
        fields = ['id', 'url', 'supply', 'demand', 'seller_price', 'buyer_price', 'seller_agent_price', 'buyer_agent_price', 'company_price']