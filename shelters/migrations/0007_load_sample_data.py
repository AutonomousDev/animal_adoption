from django.db import migrations
from django.core.management import call_command


def load_fixture(apps, schema_editor):
    call_command('loaddata', 'Shelter')


class Migration(migrations.Migration):

    dependencies = [
        ('shelters', '0006_shelter_website'),
    ]

    operations = [
        migrations.RunPython(load_fixture)
    ]
