# Generated by Django 5.0 on 2024-03-13 14:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0005_alter_linestringlocation_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='linestringlocation',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='linestringlocation',
            name='name',
        ),
        migrations.RemoveField(
            model_name='linestringlocation',
            name='question',
        ),
        migrations.RemoveField(
            model_name='pointlocation',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='pointlocation',
            name='name',
        ),
        migrations.RemoveField(
            model_name='pointlocation',
            name='question',
        ),
        migrations.RemoveField(
            model_name='polygonlocation',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='polygonlocation',
            name='name',
        ),
        migrations.RemoveField(
            model_name='polygonlocation',
            name='question',
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('answer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apiapp.answer')),
                ('lines', models.ManyToManyField(blank=True, to='apiapp.linestringlocation')),
                ('points', models.ManyToManyField(blank=True, to='apiapp.pointlocation')),
                ('polygons', models.ManyToManyField(blank=True, to='apiapp.polygonlocation')),
                ('question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apiapp.question')),
            ],
        ),
    ]