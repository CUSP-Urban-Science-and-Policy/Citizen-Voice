# Generated by Django 5.0 on 2024-03-15 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0010_alter_answer_locations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='body',
            field=models.TextField(blank=True, verbose_name='Answer Body'),
        ),
    ]