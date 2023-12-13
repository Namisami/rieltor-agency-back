import os
import csv
import io
from datetime import datetime

from config.settings import BASE_DIR
from esoft.models import Client, Agent, Object, Offer, Demand, Deal, ObjectType, District

CSV_ROOT = BASE_DIR / 'csv_data'

def run():
    with io.open(os.path.join(CSV_ROOT, 'agents.csv'), encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            Agent.objects.get_or_create(
                id=row[0],
                first_name=row[1],
                middle_name=row[2],
                last_name=row[3],
                deal_share=row[4],
            )

    with io.open(os.path.join(CSV_ROOT, 'clients.csv'), encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            Client.objects.get_or_create(
                id=row[0],
                first_name=row[1],
                middle_name=row[2],
                last_name=row[3],
                phone=row[4],
                email=row[5],
            )

    with io.open(os.path.join(CSV_ROOT, 'apartments.csv'), encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            # coordinates, _ = Coordinate.objects.get_or_create(
            #     latitude=row[5],
            #     logitude=row[6],
            # )

            object_type, _ = ObjectType.objects.get_or_create(
                name='Квартира'
            )

            Object.objects.get_or_create(
                id=row[0],
                address_city=row[1],
                address_street=row[2],
                address_house=row[3],
                address_number=row[4],
                latitude=row[5],
                logitude=row[6],
                total_area=row[7],
                rooms=row[8],
                floor=row[9],
                type=object_type
            )

    with io.open(os.path.join(CSV_ROOT, 'houses.csv'), encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            # coordinates, _ = Coordinate.objects.get_or_create(
            #     latitude=row[5],
            #     logitude=row[6],
            # )

            object_type, _ = ObjectType.objects.get_or_create(
                name='Дом'
            )

            Object.objects.get_or_create(
                id=row[0],
                address_city=row[1],
                address_street=row[2],
                address_house=row[3],
                address_number=row[4],
                latitude=row[5],
                logitude=row[6],
                total_floors=row[7],
                total_area=row[8],
                type=object_type
            )

    with io.open(os.path.join(CSV_ROOT, 'lands.csv'), encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            # coordinates, _ = Coordinate.objects.get_or_create(
            #     latitude=row[5],
            #     logitude=row[6],
            # )

            object_type, _ = ObjectType.objects.get_or_create(
                name='Участок'
            )

            Object.objects.get_or_create(
                id=row[0],
                address_city=row[1],
                address_street=row[2],
                address_house=row[3],
                address_number=row[4],
                latitude=row[5],
                logitude=row[6],
                total_area=row[7],
                type=object_type
            )

    with io.open(os.path.join(CSV_ROOT, 'districts.csv'), encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            # cords = []
            # for coordinate in row[1].split('),('):
            #     coordinate = coordinate.replace('(', '')
            #     coordinate = coordinate.replace(')', '')
            #     lat, log = coordinate.split(',')
            #     coordinates, _ = Coordinate.objects.get_or_create(
            #         latitude=lat,
            #         logitude=log,
            #     )
            #     cords.append(coordinates)

            district, _ = District.objects.get_or_create(
                name=row[0],
                area=row[1]
            )
            # for cord in cords:
            #     district.area.add(cord)

    with io.open(os.path.join(CSV_ROOT, 'apartment-demands.csv'), encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            agent = Agent.objects.get(id=row[7])
            client = Client.objects.get(id=row[8])

            i = 5
            for r in row[5:]:
                if r == '':
                    row[i] = None 
                i += 1

            Demand.objects.get_or_create(
                id=row[0],
                address_city=row[1],
                address_street=row[2],
                address_house=row[3],
                address_number=row[4],
                min_price=row[5],
                max_price=row[6],
                agent=agent,
                client=client,
                min_area=row[9],
                max_area=row[10],
                min_rooms=row[11],
                max_rooms=row[12],
                min_floor=row[13],
                max_floor=row[14],
            )

    with io.open(os.path.join(CSV_ROOT, 'house-demands.csv'), encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            agent = Agent.objects.get(id=row[7])
            client = Client.objects.get(id=row[8])
            
            i = 5
            for r in row[5:]:
                if r == '':
                    row[i] = None 
                i += 1

            Demand.objects.get_or_create(
                id=row[0],
                address_city=row[1],
                address_street=row[2],
                address_house=row[3],
                address_number=row[4],
                min_price=row[5],
                max_price=row[6],
                agent=agent,
                client=client,
                min_floors=row[9],
                max_floors=row[10],
                min_area=row[11],
                max_area=row[12],
                min_rooms=row[13],
                max_rooms=row[14],
            )

    with io.open(os.path.join(CSV_ROOT, 'land-demands.csv'), encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            agent = Agent.objects.get(id=row[7])
            client = Client.objects.get(id=row[8])

            i = 5
            for r in row[5:]:
                if r == '':
                    row[i] = None 
                i += 1

            Demand.objects.get_or_create(
                id=row[0],
                address_city=row[1],
                address_street=row[2],
                address_house=row[3],
                address_number=row[4],
                min_price=row[5],
                max_price=row[6],
                agent=agent,
                client=client,
                min_area=row[9],
                max_area=row[10],
            )

    with io.open(os.path.join(CSV_ROOT, 'supplies.csv'), encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            agent = Agent.objects.get(id=row[2])
            client = Client.objects.get(id=row[3])
            obj = Object.objects.get(id=row[4])

            Offer.objects.get_or_create(
                id=row[0],
                price=row[1],
                agent=agent,
                client=client,
                real_estate=obj
            )

    with io.open(os.path.join(CSV_ROOT, 'deals.csv'), encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            demand = Demand.objects.get(id=row[1])
            offer = Offer.objects.get(id=row[2])

            Deal.objects.get_or_create(
                id=row[0],
                demand=demand,
                supply=offer
            )
