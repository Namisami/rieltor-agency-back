from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator

class Client(models.Model):
    firstname = models.CharField(max_length=50, verbose_name='Фамилия')
    middlename = models.CharField(max_length=50, verbose_name='Имя')
    lastname = models.CharField(max_length=60, verbose_name='Отчество')
    phone = PhoneNumberField(blank=True, verbose_name='Телефон', null=True)
    email = models.EmailField(max_length = 254, verbose_name='Email', null=True)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class Agent(models.Model):
    firstname = models.CharField(max_length=50, verbose_name='Фамилия', blank=True, null=True)
    middlename = models.CharField(max_length=50, verbose_name='Имя', blank=True, null=True)
    lastname = models.CharField(max_length=60, verbose_name='Отчесвто', blank=True, null=True)
    dealshare = models.IntegerField(default=0, verbose_name='Доля от комиссии',validators=[MinValueValidator(0), MaxValueValidator(10)], help_text='Доля от комиссии должна быть от 0 ₽ до 100 ₽')
        
    class Meta:
        verbose_name = 'Риэлтор'
        verbose_name_plural = 'Риэлтора'

class Types(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')

    class Meta:
        verbose_name = 'Тип объекта'
        verbose_name_plural = 'Типы объектов'

class Object(models.Model):
    address_city = models.CharField(max_length=200, verbose_name='Город')
    address_street = models.CharField(max_length=200, verbose_name='Улица')
    address_house = models.CharField(max_length=200, verbose_name='Дом')
    address_number = models.CharField(max_length=200, verbose_name='Номер дома')
    coordinate_latitude = models.IntegerField(default=0, verbose_name='Координата широты', validators=[MinValueValidator(-90), MaxValueValidator(90)], help_text='Широта может принимать значения от -90 до +90')
    coordinate_lоgitude = models.IntegerField(default=0, verbose_name='Координата долготы', validators=[MinValueValidator(-180), MaxValueValidator(180)], help_text='Долгота может принимать значения от -180 до +180')
    totalarea = models.IntegerField(verbose_name='Площадь')
    rooms = models.IntegerField(verbose_name='Количество комнат')
    floor = models.IntegerField(verbose_name='Этаж')
    totalfloors = models.IntegerField(verbose_name='Этажность')
    types = models.ForeignKey(Types, related_name="types_object_set", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'

class Coordinate(models.Model):
    coordinate_latitude = models.ForeignKey(Object, related_name="coordinate_latitude_coordinate_set", on_delete=models.PROTECT)
    coordinate_lоgitude = models.ForeignKey(Object, related_name="coordinate_lоgitude_coordinate_set", on_delete=models.PROTECT)  

    class Meta:
        verbose_name = 'Координата'
        verbose_name_plural = 'Координаты'

class District(models.Model):
    name = models.CharField(max_length=200, verbose_name='Район')
    area = models.ForeignKey(Coordinate, related_name="area_district_set", on_delete=models.PROTECT) 

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'

class Offer(models.Model):
    client = models.ForeignKey(Client, related_name="client_offer_set", on_delete=models.PROTECT)
    agent = models.ForeignKey(Agent, related_name="agent_offer_set", on_delete=models.PROTECT)
    object = models.ForeignKey(Object, related_name="object_offer_set", on_delete=models.PROTECT)
    price = models.IntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Предложение'
        verbose_name_plural = 'Предложения'

class Need(models.Model):
    client = models.ForeignKey(Client, related_name="client_need_set", on_delete=models.PROTECT)
    agent = models.ForeignKey(Agent, related_name="agent_need_set", on_delete=models.PROTECT)
    types = models.ForeignKey(Types, related_name="types_need_set", on_delete=models.CASCADE) 
    min_price = models.IntegerField(verbose_name='Минимальная цена') 
    max_price = models.IntegerField(verbose_name='Максимальная цена') 
    min_area = models.CharField(max_length=10000000000000, verbose_name='Минимальная площадь')
    max_area = models.CharField(max_length=10000000000000, verbose_name='Максимальная площадь')
    min_room = models.IntegerField(verbose_name='Минимальное кол-во комнат')
    max_room = models.IntegerField(verbose_name='Максимальное кол-во комнат')
    min_floor = models.IntegerField(verbose_name='Минимальный этаж')
    max_floor = models.IntegerField(verbose_name='Максимальный этаж')
    min_totalfloors = models.IntegerField(verbose_name='Минимальная этажность дома')
    max_totalfloors = models.IntegerField(verbose_name='Максимальная этажность дома')

    class Meta:
        verbose_name = 'Потребность'
        verbose_name_plural = 'Потребности'

class Deal(models.Model):
    offer = models.ForeignKey(Offer, related_name="offer_deal_set", on_delete=models.PROTECT, error_messages='Запрещено удаление предложения, участвующего в сделке.')
    need = models.ForeignKey(Need, related_name="need_deal_set", on_delete=models.PROTECT, error_messages='Запрещено удаление потребности, участвующей в сделке.') 

    class Meta:
        verbose_name = 'Сделка'
        verbose_name_plural = 'Сделки' 



