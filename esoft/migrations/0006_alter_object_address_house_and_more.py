# Generated by Django 4.2 on 2023-12-14 23:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esoft', '0005_demand_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='address_house',
            field=models.CharField(max_length=200, null=True, verbose_name='Дом'),
        ),
        migrations.AlterField(
            model_name='object',
            name='address_number',
            field=models.CharField(max_length=200, null=True, verbose_name='Номер дома'),
        ),
        migrations.AlterField(
            model_name='object',
            name='latitude',
            field=models.DecimalField(decimal_places=12, max_digits=15, validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90)]),
        ),
        migrations.AlterField(
            model_name='object',
            name='logitude',
            field=models.DecimalField(decimal_places=12, max_digits=15, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)]),
        ),
    ]
