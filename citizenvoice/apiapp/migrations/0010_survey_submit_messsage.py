# Generated by Django 5.0 on 2024-07-03 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0009_alter_linefeature_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='submit_messsage',
            field=models.TextField(blank=True, default='Thank you for your participation!', verbose_name='Message to be displayed after survey is submited'),
        ),
    ]
