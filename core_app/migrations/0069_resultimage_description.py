# Generated by Django 4.0.2 on 2023-02-10 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0068_remove_additionalqualification_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultimage',
            name='description',
            field=models.CharField(default='school information', max_length=200),
        ),
    ]