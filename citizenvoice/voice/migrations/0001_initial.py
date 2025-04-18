# Generated by Django 5.0 on 2025-03-03 10:05

import django.contrib.gis.db.models.fields
import django.db.models.deletion
import uuid
import voice.models.mapview
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DashboardTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, verbose_name='topic name')),
            ],
        ),
        migrations.CreateModel(
            name='LocationCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LineFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.LineStringField(srid=4326)),
                ('annotation', models.CharField(blank=True, max_length=150, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voice.locationcollection')),
            ],
        ),
        migrations.CreateModel(
            name='MapView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Delft', max_length=150, verbose_name='Name of the MapView location')),
                ('map_service_url', models.CharField(default=voice.models.mapview.default_service_url, max_length=150, verbose_name='Map Service URL')),
                ('description', models.TextField(blank=True, max_length=200, null=True, verbose_name='Description of the MapView')),
                ('options', models.JSONField(default=voice.models.mapview.default_options, verbose_name='Map service specific options')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='voice.locationcollection')),
            ],
        ),
        migrations.CreateModel(
            name='PointFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('annotation', models.CharField(blank=True, max_length=150, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voice.locationcollection')),
            ],
        ),
        migrations.CreateModel(
            name='PolygonFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('annotation', models.CharField(blank=True, max_length=150, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voice.locationcollection')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Question')),
                ('explanation', models.TextField(blank=True, max_length=200, null=True, verbose_name='Explanation for the question')),
                ('order', models.IntegerField(verbose_name='Order of where question is placed')),
                ('required', models.BooleanField(default=True, verbose_name='Question must be filled out')),
                ('has_text_input', models.BooleanField(default=True, verbose_name='Show the input text field')),
                ('question_type', models.CharField(choices=[('text', 'text (multiple line)'), ('short-text', 'short text (one line)'), ('radio', 'radio'), ('select', 'select'), ('select-multiple', 'Select Multiple'), ('select_image', 'Select Image'), ('integer', 'integer'), ('float', 'float'), ('date', 'date')], default='text', max_length=150, verbose_name='Type of question')),
                ('choices', models.TextField(blank=True, null=True, verbose_name='Choices for answers')),
                ('is_geospatial', models.BooleanField(default=False, verbose_name='If the question must be answered geospatially or not')),
                ('mapview', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='voice.mapview')),
                ('topics', models.ManyToManyField(blank=True, to='voice.dashboardtopic', verbose_name='Topics')),
            ],
            options={
                'verbose_name': 'question',
                'verbose_name_plural': 'questions',
                'ordering': ('survey', 'order'),
            },
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date response was submitted')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last edit')),
                ('response_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True, verbose_name='Unique ID of interview')),
                ('respondent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last edited')),
                ('body', models.TextField(blank=True, verbose_name='Answer Body')),
                ('mapview', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='voice.mapview')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voice.question')),
                ('response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voice.response')),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name of the survey')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('is_published', models.BooleanField(default=False, verbose_name='Survey is visible and accessible to users')),
                ('need_logged_user', models.BooleanField(default=False, verbose_name='Only authenticated users have access to this survey')),
                ('editable_answers', models.BooleanField(default=True, verbose_name='Answers can be edited after submission')),
                ('submit_message', models.TextField(blank=True, default='Thank you for your participation!', verbose_name='Message to be displayed after survey is submitted')),
                ('publish_date', models.DateTimeField(verbose_name='Date that survey was made available')),
                ('expire_date', models.DateTimeField(verbose_name='Expiry date of survey')),
                ('public_url', models.CharField(blank=True, max_length=255, verbose_name='Public URL')),
                ('designer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='response',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='voice.survey'),
        ),
        migrations.AddField(
            model_name='question',
            name='survey',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='voice.survey'),
        ),
    ]
