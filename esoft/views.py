from rest_framework import viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from Levenshtein import distance
from rest_framework.decorators import action
from .serializers import ClientSerializers, AgentSerializers, ObjectSerializers, OfferSerializers, DemandSerializers, DealSerializers, ObjectTypeSerializers, DistrictSerializers
from .models import Client, Agent, Object, Offer, Demand, Deal, ObjectType, District

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
    
    @action(methods=['get'], detail=True)
    def deals(self, request, pk):
        offers = OfferSerializers(Offer.objects.filter(client__id=pk), many=True, context={'request': request})
        demands = DemandSerializers(Demand.objects.filter(client__id=pk), many=True, context={'request': request})
        print(offers.data, demands.data)
        return Response(data={'offers': offers.data, 'demands': demands.data})

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
    
    @action(methods=['get'], detail=True)
    def deals(self, request, pk):
        offers = OfferSerializers(Offer.objects.filter(agent__id=pk), many=True, context={'request': request})
        demands = DemandSerializers(Demand.objects.filter(agent__id=pk), many=True, context={'request': request})
        print(offers.data, demands.data)
        return Response(data={'offers': offers.data, 'demands': demands.data})


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializers


class ObjectTypeViewSet(viewsets.ModelViewSet):
    queryset = ObjectType.objects.all()
    serializer_class = ObjectTypeSerializers


class ObjectViewSet(viewsets.ModelViewSet):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializers
    
    def get_queryset(self):
        self.queryset = Object.objects.all()
        district = self.request.query_params.get('district')
        if district is not None:
            district_obj = District.objects.get(name=district)
            # for district_obj in District.objects.all():
            cords = cord_string_into_list(district_obj.area)
            min_lat = 10000
            min_log = 10000
            max_lat = 0
            max_log = 0
            for lat, log in cords:
                if lat < min_lat:
                    min_lat = lat
                if log < min_log:
                    min_log = log
                if lat > max_lat:
                    max_lat = lat
                if log > max_log:
                    max_log = log
            print(min_log, min_lat, max_log, max_lat)
            self.queryset = [query for query in self.queryset if (query.latitude in [min_lat, max_lat]) and (query.logitude in [min_log, max_log])]
        city = self.request.query_params.get('city')
        if city is not None:
            self.queryset = [query for query in self.queryset if distance(query.address_city, city) <= 3]
        obj_type = self.request.query_params.get('type')
        if obj_type is not None:
            self.queryset = [query for query in self.queryset if query.type.name == obj_type]
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


def cord_string_into_list(cord_str):
    cords = []
    for coordinate in cord_str.split('),('):
        coordinate = coordinate.replace('(', '')
        coordinate = coordinate.replace(')', '')
        lat, log = coordinate.split(',')
        cords.append((float(lat), float(log)))
    return cords
