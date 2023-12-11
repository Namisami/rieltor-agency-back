# Generated by Django 4.2 on 2023-12-07 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('esoft', '0002_agent_coordinate_deal_district_need_object_offer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordinate',
            name='coordinate_latitude',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='coordinate_latitude_coordinate_set', to='esoft.object'),
        ),
        migrations.AlterField(
            model_name='coordinate',
            name='coordinate_lоgitude',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='coordinate_lоgitude_coordinate_set', to='esoft.object'),
        ),
        migrations.AlterField(
            model_name='district',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='area_district_set', to='esoft.coordinate'),
        ),
    ]