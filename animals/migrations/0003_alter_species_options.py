# Generated by Django 4.2.2 on 2023-07-04 01:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0002_rename_animals_animal'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='species',
            options={'verbose_name_plural': 'species'},
        ),
    ]
