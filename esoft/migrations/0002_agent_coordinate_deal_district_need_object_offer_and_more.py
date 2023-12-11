# Generated by Django 4.2.1 on 2023-11-29 18:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('esoft', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=50, null=True, verbose_name='Фамилия')),
                ('middlename', models.CharField(blank=True, max_length=50, null=True, verbose_name='Имя')),
                ('lastname', models.CharField(blank=True, max_length=60, null=True, verbose_name='Отчесвто')),
                ('dealshare', models.IntegerField(default=0, help_text='Доля от комиссии должна быть от 0 ₽ до 100 ₽', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Доля от комиссии')),
            ],
            options={
                'verbose_name': 'Риэлтор',
                'verbose_name_plural': 'Риэлтора',
            },
        ),
        migrations.CreateModel(
            name='Coordinate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordinate_latitude', models.IntegerField(default=0, help_text='Широта может принимать значения от -90 до +90', validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90)], verbose_name='Координата широты')),
                ('coordinate_lоgitude', models.IntegerField(default=0, help_text='Долгота может принимать значения от -180 до +180', validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)], verbose_name='Координата долготы')),
            ],
            options={
                'verbose_name': 'Координата',
                'verbose_name_plural': 'Координаты',
            },
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Сделка',
                'verbose_name_plural': 'Сделки',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Район')),
                ('area', models.CharField(max_length=10000000000000, verbose_name='Площадь')),
            ],
            options={
                'verbose_name': 'Район',
                'verbose_name_plural': 'Районы',
            },
        ),
        migrations.CreateModel(
            name='Need',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_price', models.IntegerField(verbose_name='Минимальная цена')),
                ('max_price', models.IntegerField(verbose_name='Максимальная цена')),
                ('min_area', models.CharField(max_length=10000000000000, verbose_name='Минимальная площадь')),
                ('max_area', models.CharField(max_length=10000000000000, verbose_name='Максимальная площадь')),
                ('min_room', models.IntegerField(verbose_name='Минимальное кол-во комнат')),
                ('max_room', models.IntegerField(verbose_name='Максимальное кол-во комнат')),
                ('min_floor', models.IntegerField(verbose_name='Минимальный этаж')),
                ('max_floor', models.IntegerField(verbose_name='Максимальный этаж')),
                ('min_totalfloors', models.IntegerField(verbose_name='Минимальная этажность дома')),
                ('max_totalfloors', models.IntegerField(verbose_name='Максимальная этажность дома')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='agent_need_set', to='esoft.agent')),
            ],
            options={
                'verbose_name': 'Потребность',
                'verbose_name_plural': 'Потребности',
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
                ('coordinate_latitude', models.IntegerField(default=0, help_text='Широта может принимать значения от -90 до +90', validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90)], verbose_name='Координата широты')),
                ('coordinate_lоgitude', models.IntegerField(default=0, help_text='Долгота может принимать значения от -180 до +180', validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)], verbose_name='Координата долготы')),
                ('totalarea', models.IntegerField(verbose_name='Площадь')),
                ('rooms', models.IntegerField(verbose_name='Количество комнат')),
                ('floor', models.IntegerField(verbose_name='Этаж')),
                ('totalfloors', models.IntegerField(verbose_name='Этажность')),
            ],
            options={
                'verbose_name': 'Объект',
                'verbose_name_plural': 'Объекты',
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='agent_offer_set', to='esoft.agent')),
            ],
            options={
                'verbose_name': 'Предложение',
                'verbose_name_plural': 'Предложения',
            },
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип объекта',
                'verbose_name_plural': 'Типы объектов',
            },
        ),
        migrations.RemoveField(
            model_name='apartament',
            name='numb_apartament',
        ),
        migrations.RemoveField(
            model_name='apartament',
            name='sqmt',
        ),
        migrations.RemoveField(
            model_name='home',
            name='numb_home',
        ),
        migrations.RemoveField(
            model_name='home',
            name='sqmt',
        ),
        migrations.RemoveField(
            model_name='immovables',
            name='address',
        ),
        migrations.DeleteModel(
            name='Realtor',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='last_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='surname',
            new_name='lastname',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='first_name',
            new_name='middlename',
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Телефон'),
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Apartament',
        ),
        migrations.DeleteModel(
            name='Earth',
        ),
        migrations.DeleteModel(
            name='Home',
        ),
        migrations.DeleteModel(
            name='Immovables',
        ),
        migrations.AddField(
            model_name='offer',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='client_offer_set', to='esoft.client'),
        ),
        migrations.AddField(
            model_name='offer',
            name='object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='object_offer_set', to='esoft.object'),
        ),
        migrations.AddField(
            model_name='object',
            name='types',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='types_object_set', to='esoft.types'),
        ),
        migrations.AddField(
            model_name='need',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='client_need_set', to='esoft.client'),
        ),
        migrations.AddField(
            model_name='need',
            name='types',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='types_need_set', to='esoft.types'),
        ),
        migrations.AddField(
            model_name='deal',
            name='need',
            field=models.ForeignKey(error_messages='Запрещено удаление потребности, участвующей в сделке.', on_delete=django.db.models.deletion.PROTECT, related_name='need_deal_set', to='esoft.need'),
        ),
        migrations.AddField(
            model_name='deal',
            name='offer',
            field=models.ForeignKey(error_messages='Запрещено удаление предложения, участвующего в сделке.', on_delete=django.db.models.deletion.PROTECT, related_name='offer_deal_set', to='esoft.offer'),
        ),
    ]