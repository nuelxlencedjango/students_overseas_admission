# Generated by Django 4.0.2 on 2022-09-17 01:25

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_remove_partnersdetails_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='partnersdetails',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2),
        ),
    ]
