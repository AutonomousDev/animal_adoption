# Generated by Django 4.2.2 on 2023-07-14 15:41

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0003_post_animal'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='News',
        ),
    ]
