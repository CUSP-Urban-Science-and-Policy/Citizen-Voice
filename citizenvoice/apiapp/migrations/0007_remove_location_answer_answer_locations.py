# Generated by Django 5.0 on 2024-03-13 16:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0006_remove_linestringlocation_answer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='answer',
        ),
        migrations.AddField(
            model_name='answer',
            name='locations',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apiapp.location'),
        ),
    ]