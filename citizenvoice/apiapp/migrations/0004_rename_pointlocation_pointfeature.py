# Generated by Django 5.0 on 2024-03-27 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0003_mapview_location_collection'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PointLocation',
            new_name='PointFeature',
        ),
    ]