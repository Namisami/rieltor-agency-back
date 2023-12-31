# Generated by Django 4.2 on 2023-12-11 13:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Фамилия')),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=60, null=True, verbose_name='Отчесвто')),
                ('deal_share', models.IntegerField(default=0, help_text='Доля от комиссии должна быть от 0 ₽ до 100%', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Доля от комиссии')),
            ],
            options={
                'verbose_name': 'Риэлтор',
                'verbose_name_plural': 'Риэлтора',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('middle_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=60, verbose_name='Отчество')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Coordinate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logitude', models.DecimalField(decimal_places=6, max_digits=9, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)])),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9, validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90)])),
            ],
            options={
                'verbose_name': 'Координата',
                'verbose_name_plural': 'Координаты',
            },
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_city', models.CharField(max_length=200, verbose_name='Город')),
                ('address_street', models.CharField(max_length=200, verbose_name='Улица')),
                ('address_house', models.CharField(max_length=200, verbose_name='Дом')),
                ('address_number', models.CharField(max_length=200, verbose_name='Номер дома')),
                ('total_area', models.IntegerField(verbose_name='Площадь')),
                ('rooms', models.IntegerField(null=True, verbose_name='Количество комнат')),
                ('floor', models.IntegerField(null=True, verbose_name='Этаж')),
                ('total_floors', models.IntegerField(null=True, verbose_name='Этажность')),
                ('coordinates', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='esoft.coordinate', verbose_name='Координаты')),
            ],
            options={
                'verbose_name': 'Объект недвижимости',
                'verbose_name_plural': 'Объекты недвижимости',
            },
        ),
        migrations.CreateModel(
            name='ObjectType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Тип недвижимости',
                'verbose_name_plural': 'Типы недвижимости',
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='esoft.agent', verbose_name='Риэлтор')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='esoft.client', verbose_name='Покупатель')),
                ('real_estate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='esoft.object', verbose_name='Недвижимость')),
            ],
            options={
                'verbose_name': 'Предложение',
                'verbose_name_plural': 'Предложения',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Район')),
                ('area', models.ManyToManyField(to='esoft.coordinate', verbose_name='Координаты')),
            ],
            options={
                'verbose_name': 'Район',
                'verbose_name_plural': 'Районы',
            },
        ),
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_city', models.CharField(blank=True, max_length=200, verbose_name='Город')),
                ('address_street', models.CharField(blank=True, max_length=200, verbose_name='Улица')),
                ('address_house', models.CharField(blank=True, max_length=200, verbose_name='Дом')),
                ('address_number', models.CharField(blank=True, max_length=200, verbose_name='Номер дома')),
                ('min_price', models.IntegerField(null=True, verbose_name='Минимальная цена')),
                ('max_price', models.IntegerField(null=True, verbose_name='Максимальная цена')),
                ('min_area', models.IntegerField(null=True, verbose_name='Минимальная площадь')),
                ('max_area', models.IntegerField(null=True, verbose_name='Максимальная площадь')),
                ('min_rooms', models.IntegerField(null=True, verbose_name='Минимальное кол-во комнат')),
                ('max_rooms', models.IntegerField(null=True, verbose_name='Максимальное кол-во комнат')),
                ('min_floor', models.IntegerField(null=True, verbose_name='Минимальный этаж')),
                ('max_floor', models.IntegerField(null=True, verbose_name='Максимальный этаж')),
                ('min_floors', models.IntegerField(null=True, verbose_name='Минимальное кол-во этажей')),
                ('max_floors', models.IntegerField(null=True, verbose_name='Максимальнле кол-во этажей')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='esoft.agent', verbose_name='Риэлтор')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='esoft.client', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Спрос недвижимости',
                'verbose_name_plural': 'Спрос недвижимости',
            },
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('demand', models.ForeignKey(error_messages='Запрещено удаление потребности, участвующей в сделке.', on_delete=django.db.models.deletion.PROTECT, to='esoft.demand')),
                ('supply', models.ForeignKey(error_messages='Запрещено удаление предложения, участвующего в сделке.', on_delete=django.db.models.deletion.PROTECT, to='esoft.offer')),
            ],
            options={
                'verbose_name': 'Сделка',
                'verbose_name_plural': 'Сделки',
            },
        ),
    ]
