# Generated by Django 2.1 on 2018-09-04 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0002_remove_station_id_station'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='station',
            options={'ordering': ['date'], 'verbose_name': 'station', 'verbose_name_plural': 'stations'},
        ),
    ]
