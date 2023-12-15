from rest_framework import viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from Levenshtein import distance
from django.db.models import Q
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
            self.queryset = [query for query in self.queryset if distance(query.first_name, first_name) <= 3 and distance(query.last_name, last_name) <= 3 and distance(query.middle_name, middle_name) <= 3]
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
            self.queryset = [query for query in self.queryset if distance(query.first_name, first_name) <= 3 and distance(query.last_name, last_name) <= 3 and distance(query.middle_name, middle_name) <= 3]
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
            self.queryset = [query for query in self.queryset 
                             if ((min_lat <= query.latitude) and (query.latitude <= max_lat)) 
                             and ((min_log <= query.logitude) and (query.logitude <= max_log))]
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

    @action(methods=['get'], detail=True)
    def approach(self, request, pk):
        offer = Offer.objects.get(id=pk)
        demands_all = Demand.objects.all()
        demands = []
        city = offer.real_estate.address_city
        if city:
            demands = demands_all.filter(
                Q(address_city=city) | Q(address_city__exact=''),
            )
            if demands.count() != 0:
                demands_all = demands
        street = offer.real_estate.address_street
        if street:
            demands = demands_all.filter(
                Q(address_street=street) | Q(address_street__exact=''),
            )
            if demands.count() != 0:
                demands_all = demands
        house = offer.real_estate.address_house
        if house:
            demands = demands_all.filter(
                Q(address_house=house) | Q(address_house__exact=''),
            )
            if demands.count() != 0:
                demands_all = demands
        number = offer.real_estate.address_number
        if number:
            demands = demands_all.filter(
                Q(address_number=number) | Q(address_number__exact=''),
            )
            if demands.count() != 0:
                demands_all = demands
        type = offer.real_estate.type
        if type:
            demands = demands_all.filter(
                Q(type=type) | Q(type__isnull=True),
            )
            if demands.count() != 0:
                demands_all = demands
        price = offer.price
        if price:
            demands = demands_all.filter(
                Q(min_price__lte=price) | Q(min_price__isnull=True),
                Q(max_price__gte=price) | Q(max_price__isnull=True),
            )
            if demands.count() != 0:
                demands_all = demands
        area = offer.real_estate.total_area
        if area:
            demands = demands_all.filter(
                Q(min_area__lte=area) | Q(min_area__isnull=True),
                Q(max_area__gte=area) | Q(max_area__isnull=True),
            )
            if demands.count() != 0:
                demands_all = demands
        rooms = offer.real_estate.rooms
        if rooms:
            demands = demands_all.filter(
                Q(min_rooms__lte=rooms) | Q(min_rooms__isnull=True),
                Q(max_rooms__gte=rooms) | Q(max_rooms__isnull=True),
            )
            if demands.count() != 0:
                demands_all = demands
        floor = offer.real_estate.floor
        if floor:
            demands = demands_all.filter(
                Q(min_floor__lte=floor) | Q(min_floor__isnull=True),
                Q(max_floor__gte=floor) | Q(max_floor__isnull=True),
            )
            if demands.count() != 0:
                demands_all = demands
        total_floors = offer.real_estate.total_floors
        if total_floors:
            demands = demands_all.filter(
                Q(min_floors__lte=total_floors) | Q(min_floors__isnull=True),
                Q(max_floors__gte=total_floors) | Q(max_floors__isnull=True),
            )
            if demands.count() != 0:
                demands_all = demands
        
        demands = DemandSerializers(demands_all, many=True, context={'request': request})
        return Response(demands.data)


class DemandViewSet(viewsets.ModelViewSet):
    queryset = Demand.objects.all()
    serializer_class = DemandSerializers

    @action(methods=['get'], detail=True)
    def approach(self, request, pk):
        demand = Demand.objects.get(id=pk)
        offers_all = Offer.objects.all()
        offers = []
        city = demand.address_city
        if city:
            offers = offers_all.filter(
                Q(real_estate__address_city=city) | Q(real_estate__address_city__exact=''),
            )
            if offers.count() != 0:
                offers_all = offers
        street = demand.address_street
        if street:
            offers = offers_all.filter(
                Q(real_estate__address_street=street) | Q(real_estate__address_street__exact=''),
            )
            if offers.count() != 0:
                offers_all = offers
        house = demand.address_house
        if house:
            offers = offers_all.filter(
                Q(real_estate__address_house=house) | Q(real_estate__address_house__exact=''),
            )
            if offers.count() != 0:
                offers_all = offers
        number = demand.address_number
        if number:
            offers = offers_all.filter(
                Q(real_estate__address_number=number) | Q(real_estate__address_number__exact=''),
            )
            if offers.count() != 0:
                offers_all = offers
        type = demand.type
        if type:
            offers = offers_all.filter(
                Q(real_estate__type=type) | Q(real_estate__type__isnull=True),
            )
            if offers.count() != 0:
                offers_all = offers
        min_price = demand.min_price
        if min_price:
            offers = offers_all.filter(
                Q(price__gte=min_price) | Q(price__isnull=True),
            )
            if offers.count() != 0:
                offers_all = offers
        max_price = demand.max_price
        if max_price:
            offers = offers_all.filter(
                Q(price__lte=min_price) | Q(price__isnull=True),
            )
            if offers.count() != 0:
                offers_all = offers
        min_area = demand.min_area
        if min_area:
            offers = offers_all.filter(
                Q(real_estate__total_area__gte=min_area) | Q(real_estate__total_area__isnull=True),
            )
            if offers.count() != 0:
                offers_all = offers
        max_area = demand.max_area
        if max_area:
            offers = offers_all.filter(
                Q(real_estate__total_area__lte=max_area) | Q(real_estate__total_area__isnull=True),
            )
            if offers.count() != 0:
                offers_all = offers
        min_rooms = demand.min_rooms
        if min_rooms:
            offers = offers_all.filter(
                Q(real_estate__rooms__gte=min_rooms) | Q(real_estate__rooms__isnull=True),
            )
            if offers.count() != 0:
                offers_all = offers
        max_rooms = demand.max_rooms
        if min_rooms:
            offers = offers_all.filter(
                Q(real_estate__rooms__lte=max_rooms) | Q(real_estate__rooms__isnull=True),
            )
            if offers.count() != 0:
                offers_all = offers
        min_floor = demand.min_floor
        if min_floor:
            offers = offers_all.filter(
                Q(real_estate__floor__gte=min_floor) | Q(real_estate__floor__isnull=True),
            )
            if offers.count() != 0:
                offers_all = offers
        max_floor = demand.max_floor
        if max_floor:
            offers = offers_all.filter(
                Q(real_estate__floor__lte=max_floor) | Q(real_estate__floor__isnull=True),
            )
            if offers.count() != 0:
                offers_all = offers
        min_floors = demand.min_floors
        if min_floors:
            offers = offers_all.filter(
                Q(real_estate__total_floors__gte=min_floors) | Q(real_estate__total_floors__isnull=True),
            )
            if offers.count() != 0:
                offers_all = offers
        max_floors = demand.max_floors
        if max_floors:
            offers = offers_all.filter(
                Q(real_estate__total_floors__lte=max_floors) | Q(real_estate__total_floors__isnull=True),
            )
            if offers.count() != 0:
                offers_all = offers
        
        offers = OfferSerializers(offers_all, many=True, context={'request': request})
        return Response(offers.data)

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
