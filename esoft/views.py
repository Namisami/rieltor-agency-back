from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from Levenshtein import distance
from .serializers import ClientSerializers, AgentSerializers, ObjectSerializers, OfferSerializers, NeedSerializers, DealSerializers, TypesSerializers
from .models import Client, Agent, Object, Offer, Need, Deal, Types

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializers

    def get_queryset(self):
        fio = self.request.query_params.get('fio')
        if fio is not None:
            first_name, middle_name, last_name = fio.split(' ')
            self.queryset = [query for query in self.queryset if distance(query.firstname, first_name) <= 3 and distance(query.lastname, last_name) <= 3 and distance(query.middlename, middle_name) <= 3]
        return self.queryset

class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializers
    
    def get_queryset(self):
        fio = self.request.query_params.get('fio')
        if fio is not None:
            first_name, middle_name, last_name = fio.split(' ')
            self.queryset = [query for query in self.queryset if distance(query.firstname, first_name) <= 3 and distance(query.lastname, last_name) <= 3 and distance(query.middlename, middle_name) <= 3]
        return self.queryset

class TypesViewSet(viewsets.ModelViewSet):
    queryset = Types.objects.all()
    serializer_class = TypesSerializers

class ObjectViewSet(viewsets.ModelViewSet):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['types', 'address_street', 'address_city', 'address_house', 'address_number']

class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializers

class NeedViewSet(viewsets.ModelViewSet):
    queryset = Need.objects.all()
    serializer_class = NeedSerializers

class DealViewSet(viewsets.ModelViewSet):
    queryset = Deal.objects.all()
    serializer_class = DealSerializers



