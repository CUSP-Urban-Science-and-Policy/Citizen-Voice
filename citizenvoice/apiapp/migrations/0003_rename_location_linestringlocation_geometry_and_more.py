# Generated by Django 5.0 on 2024-03-13 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0002_linestringlocation_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='linestringlocation',
            old_name='location',
            new_name='geometry',
        ),
        migrations.RenameField(
            model_name='pointlocation',
            old_name='location',
            new_name='geometry',
        ),
        migrations.RenameField(
            model_name='polygonlocation',
            old_name='location',
            new_name='geometry',
        ),
    ]