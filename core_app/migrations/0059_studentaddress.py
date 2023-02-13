# Generated by Django 4.0.2 on 2023-01-23 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core_app', '0058_delete_studentaddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('street', models.CharField(max_length=200)),
                ('street_two', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('postal_code', models.CharField(max_length=200, null=True)),
                ('nationality', django_countries.fields.CountryField(max_length=2)),
                ('agent_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='address', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Student Address',
            },
        ),
    ]
