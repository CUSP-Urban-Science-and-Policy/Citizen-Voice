# Generated by Django 5.0 on 2024-07-03 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0010_survey_submit_messsage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='survey',
            old_name='submit_messsage',
            new_name='submit_message',
        ),
    ]
