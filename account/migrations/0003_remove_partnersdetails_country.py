# Generated by Django 4.0.2 on 2022-09-17 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_countrynames_alter_partnersdetails_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partnersdetails',
            name='country',
        ),
    ]
