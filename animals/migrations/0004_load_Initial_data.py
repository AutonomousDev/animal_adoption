# Generated by Django 4.1.3 on 2023-01-13 06:11

from django.db import migrations
from django.core.management import call_command


def load_fixture(apps, schema_editor):
    call_command('loaddata', 'Species')
    call_command('loaddata', 'Animals')


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
        ('animals', '0002_rename_animals_animal'),
        ('animals', '0003_alter_species_options')
    ]

    operations = [
        migrations.RunPython(load_fixture)
    ]
