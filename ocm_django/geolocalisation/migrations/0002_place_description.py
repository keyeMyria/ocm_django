# Generated by Django 2.1 on 2018-08-27 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geolocalisation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
