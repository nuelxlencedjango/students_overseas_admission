# Generated by Django 4.0.2 on 2022-12-03 07:27

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0035_alter_scholarship_detail_alter_scholarship_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholarship',
            name='img',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
    ]