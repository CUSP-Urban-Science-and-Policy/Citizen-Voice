# Generated by Django 5.0 on 2024-02-28 08:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0006_answer_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='response',
            field=models.ForeignKey(default='0122260b-3fcc-477e-85d2-fe43f0611b45', on_delete=django.db.models.deletion.CASCADE, to='apiapp.response'),
        ),
    ]