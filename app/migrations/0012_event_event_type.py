# Generated by Django 5.0.4 on 2024-06-05 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_event_date_remove_event_event_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.CharField(choices=[('beca', 'Beca'), ('pasantia', 'Pasantía'), ('evento', 'Evento')], default='evento', max_length=20),
        ),
    ]
