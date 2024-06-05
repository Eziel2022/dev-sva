# Generated by Django 5.0.4 on 2024-06-05 03:55

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_alumno_dni'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='image',
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.CharField(choices=[('pasantia', 'Pasantía'), ('beca', 'Beca'), ('evento', 'Evento')], default='evento', max_length=10),
        ),
        migrations.AlterField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
