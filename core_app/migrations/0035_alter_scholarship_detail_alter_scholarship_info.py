# Generated by Django 4.0.2 on 2022-11-29 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0034_courses_commission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholarship',
            name='detail',
            field=models.TextField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='info',
            field=models.TextField(blank=True, max_length=1500, null=True),
        ),
    ]
