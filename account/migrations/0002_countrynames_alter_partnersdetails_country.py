# Generated by Django 4.0.2 on 2022-09-17 00:51

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryNames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
            ],
        ),
       #= migrations.AlterField(
        #    model_name='partnersdetails',
          #  name='country',
           # field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.countrynames'),
        #),
    ]
