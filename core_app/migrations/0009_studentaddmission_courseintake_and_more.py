# Generated by Django 4.0.2 on 2022-09-22 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0008_studentaddmission'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentaddmission',
            name='courseIntake',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='studentaddmission',
            name='courseType',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='studentaddmission',
            name='status',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
