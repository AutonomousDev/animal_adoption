# Generated by Django 4.2.2 on 2023-07-10 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0003_alter_species_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='availability',
            options={'verbose_name_plural': 'availabilities'},
        ),
    ]
