# Generated by Django 5.0.4 on 2024-06-05 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_beca'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Beca',
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_type',
        ),
    ]
