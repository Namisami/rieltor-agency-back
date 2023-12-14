from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.contenttypes.fields import GenericForeignKey

class Client(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=60, verbose_name='Отчество')
    phone = PhoneNumberField(blank=True, verbose_name='Телефон', null=True)
    email = models.EmailField(max_length = 254, verbose_name='Email', null=True, blank=True)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'
    

class Agent(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Фамилия', blank=True, null=True)
    middle_name = models.CharField(max_length=50, verbose_name='Имя', blank=True, null=True)
    last_name = models.CharField(max_length=60, verbose_name='Отчесвто', blank=True, null=True)
    deal_share = models.IntegerField(default=0, verbose_name='Доля от комиссии',validators=[MinValueValidator(0), MaxValueValidator(100)], help_text='Доля от комиссии должна быть от 0 ₽ до 100%')
        
    class Meta:
        verbose_name = 'Риэлтор'
        verbose_name_plural = 'Риэлтора'
        
    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'


# class Coordinate(models.Model):
#     logitude = models.DecimalField(max_digits=9, decimal_places=6, validators=[MinValueValidator(-180), MaxValueValidator(180)])
#     latitude = models.DecimalField(max_digits=9, decimal_places=6, validators=[MinValueValidator(-90), MaxValueValidator(90)])

#     class Meta:
#         verbose_name = 'Координата'
#         verbose_name_plural = 'Координаты'

    # def __str__(self):
    #     return f'({self.latitude}; {self.logitude})'

class ObjectType(models.Model):
    name = models.CharField(max_length=255, verbose_name='Тип')

    class Meta:
        verbose_name = 'Тип недвижимости'
        verbose_name_plural = 'Типы недвижимости'

    def __str__(self):
        return self.name
    

class Object(models.Model):
    address_city = models.CharField(max_length=200, verbose_name='Город')
    address_street = models.CharField(max_length=200, verbose_name='Улица')
    address_house = models.CharField(max_length=200, verbose_name='Дом', null=True)
    address_number = models.CharField(max_length=200, verbose_name='Номер дома', null=True)
    latitude = models.DecimalField(max_digits=15, decimal_places=12, validators=[MinValueValidator(-90), MaxValueValidator(90)])
    logitude = models.DecimalField(max_digits=15, decimal_places=12, validators=[MinValueValidator(-180), MaxValueValidator(180)])
    total_area = models.DecimalField(verbose_name='Площадь', max_digits=4, decimal_places=1)

    rooms = models.IntegerField(verbose_name='Количество комнат', null=True)
    floor = models.IntegerField(verbose_name='Этаж', null=True)

    total_floors = models.IntegerField(verbose_name='Этажность', null=True)
    
    type = models.ForeignKey(ObjectType, on_delete=models.PROTECT, verbose_name='Тип недвижимости')

    class Meta:
        verbose_name = 'Объект недвижимости'
        verbose_name_plural = 'Объекты недвижимости'
        
    def __str__(self):
        return f'{self.address_city}, {self.address_street}, {self.address_house}, {self.address_number}'


class District(models.Model):
    name = models.CharField(max_length=200, verbose_name='Район')
    area = models.TextField(verbose_name='Координаты') 

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'

    def __str__(self):
        return self.name


class Demand(models.Model):
    address_city = models.CharField(max_length=200, verbose_name='Город', blank=True)
    address_street = models.CharField(max_length=200, verbose_name='Улица', blank=True)
    address_house = models.CharField(max_length=200, verbose_name='Дом', blank=True)
    address_number = models.CharField(max_length=200, verbose_name='Номер дома', blank=True)
    min_price = models.IntegerField(verbose_name='Минимальная цена', null=True) 
    max_price = models.IntegerField(verbose_name='Максимальная цена', null=True)
    agent = models.ForeignKey(to=Agent, on_delete=models.PROTECT, verbose_name='Риэлтор')
    client = models.ForeignKey(to=Client, on_delete=models.PROTECT, verbose_name='Клиент')
    type = models.ForeignKey(to=ObjectType, on_delete=models.PROTECT, verbose_name='Тип объекта недвижимости')
    min_area = models.IntegerField(verbose_name='Минимальная площадь', null=True)
    max_area = models.IntegerField(verbose_name='Максимальная площадь', null=True)

    min_rooms = models.IntegerField(verbose_name='Минимальное кол-во комнат', null=True)
    max_rooms = models.IntegerField(verbose_name='Максимальное кол-во комнат', null=True)
    min_floor = models.IntegerField(verbose_name='Минимальный этаж', null=True)
    max_floor = models.IntegerField(verbose_name='Максимальный этаж', null=True)

    min_floors = models.IntegerField(verbose_name='Минимальное кол-во этажей', null=True)
    max_floors = models.IntegerField(verbose_name='Максимальнле кол-во этажей', null=True)

    class Meta:
        verbose_name = 'Спрос недвижимости'
        verbose_name_plural = 'Спрос недвижимости'

    def __str__(self):
        return f'{self.client}'


class Offer(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT, verbose_name='Покупатель')
    agent = models.ForeignKey(Agent, on_delete=models.PROTECT, verbose_name='Риэлтор')
    real_estate = models.ForeignKey(Object, on_delete=models.CASCADE, verbose_name='Недвижимость')
    price = models.IntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Предложение'
        verbose_name_plural = 'Предложения'

    def __str__(self):
        return f'{self.agent} -> {self.client}'


class Deal(models.Model):
    supply = models.ForeignKey(Offer, on_delete=models.PROTECT, error_messages='Запрещено удаление предложения, участвующего в сделке.')
    demand = models.ForeignKey(Demand, on_delete=models.PROTECT, error_messages='Запрещено удаление потребности, участвующей в сделке.') 

    class Meta:
        verbose_name = 'Сделка'
        verbose_name_plural = 'Сделки' 
