# Generated by Django 4.2.2 on 2023-07-13 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0004_load_Initial_data'),
        ('news', '0002_rename_posts_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='animal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='animals.animal'),
        ),
    ]