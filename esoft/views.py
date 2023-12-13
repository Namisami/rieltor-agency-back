from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from Levenshtein import distance
from .serializers import ClientSerializers, AgentSerializers, ObjectSerializers, OfferSerializers, DemandSerializers, DealSerializers, ObjectTypeSerializers
from .models import Client, Agent, Object, Offer, Demand, Deal, ObjectType

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializers

    def get_queryset(self):
        self.queryset = Client.objects.all()
        fio = self.request.query_params.get('fio')
        if fio is not None:
            first_name, middle_name, last_name = fio.split(' ')
            self.queryset = [query for query in self.queryset if distance(query.firstname, first_name) <= 3 and distance(query.lastname, last_name) <= 3 and distance(query.middlename, middle_name) <= 3]
        return self.queryset

class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializers
    
    def get_queryset(self):
        self.queryset = Agent.objects.all()
        fio = self.request.query_params.get('fio')
        if fio is not None:
            first_name, middle_name, last_name = fio.split(' ')
            self.queryset = [query for query in self.queryset if distance(query.firstname, first_name) <= 3 and distance(query.lastname, last_name) <= 3 and distance(query.middlename, middle_name) <= 3]
        return self.queryset

class ObjectTypeViewSet(viewsets.ModelViewSet):
    queryset = ObjectType.objects.all()
    serializer_class = ObjectTypeSerializers

class ObjectViewSet(viewsets.ModelViewSet):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ObjectType', 'address_street', 'address_city', 'address_house', 'address_number']
        
    def get_queryset(self):
        self.queryset = Object.objects.all()
        city = self.request.query_params.get('city')
        if city is not None:
            self.queryset = [query for query in self.queryset if distance(query.address_city, city) <= 3]
        street = self.request.query_params.get('street')
        if street is not None:
            self.queryset = [query for query in self.queryset if distance(query.address_street, street) <= 3]
        house = self.request.query_params.get('house')
        if house is not None:
            self.queryset = [query for query in self.queryset if distance(query.address_house, house) <= 1]
        number = self.request.query_params.get('number')
        if number is not None:
            self.queryset = [query for query in self.queryset if distance(query.address_number, number) <= 1]
        return self.queryset

class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializers

class DemandViewSet(viewsets.ModelViewSet):
    queryset = Demand.objects.all()
    serializer_class = DemandSerializers

class DealViewSet(viewsets.ModelViewSet):
    queryset = Deal.objects.all()
    serializer_class = DealSerializers



