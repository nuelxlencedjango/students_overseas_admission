# Generated by Django 4.0.2 on 2022-10-19 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0018_emergencycontact_student_studentaddress_student_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emergencycontact',
            name='student',
        ),
        migrations.RemoveField(
            model_name='studentaddress',
            name='student',
        ),
        migrations.RemoveField(
            model_name='studentpassort',
            name='student',
        ),
        migrations.RemoveField(
            model_name='workexperience',
            name='student',
        ),
    ]