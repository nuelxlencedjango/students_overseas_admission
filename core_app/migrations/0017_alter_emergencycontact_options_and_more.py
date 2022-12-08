# Generated by Django 4.0.2 on 2022-10-19 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0016_workexperience_studentpassort_studentaddress_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emergencycontact',
            options={'verbose_name_plural': 'Emergency Contact'},
        ),
        migrations.AlterModelOptions(
            name='studentaddmission',
            options={'verbose_name_plural': 'Student Addmission'},
        ),
        migrations.AlterModelOptions(
            name='studentaddress',
            options={'verbose_name_plural': 'Student Address'},
        ),
        migrations.AlterModelOptions(
            name='studentapplication',
            options={'verbose_name_plural': 'Student Application'},
        ),
        migrations.AlterModelOptions(
            name='studentpassort',
            options={'verbose_name_plural': 'Student Passport'},
        ),
        migrations.AlterModelOptions(
            name='workexperience',
            options={'verbose_name_plural': 'Work EXperience'},
        ),
        migrations.RemoveField(
            model_name='emergencycontact',
            name='studentName',
        ),
        migrations.RemoveField(
            model_name='studentaddress',
            name='studentName',
        ),
        migrations.RemoveField(
            model_name='studentpassort',
            name='studentName',
        ),
        migrations.RemoveField(
            model_name='workexperience',
            name='studentName',
        ),
    ]