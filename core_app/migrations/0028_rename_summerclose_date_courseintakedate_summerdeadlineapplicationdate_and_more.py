# Generated by Django 4.0.2 on 2022-11-29 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0027_remove_courses_courseintake_courseintakedate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseintakedate',
            old_name='summerClose_date',
            new_name='summerDeadlineApplicationDate',
        ),
        migrations.RenameField(
            model_name='courseintakedate',
            old_name='summerDeadline',
            new_name='summerEndStart_date',
        ),
        migrations.RenameField(
            model_name='courseintakedate',
            old_name='University',
            new_name='university',
        ),
        migrations.RenameField(
            model_name='courseintakedate',
            old_name='winterClose_date',
            new_name='winterApplicationDeadline',
        ),
        migrations.RenameField(
            model_name='courseintakedate',
            old_name='winterDeadline',
            new_name='winterEndStart_date',
        ),
        migrations.RenameField(
            model_name='courseintakedate',
            old_name='winter_openApplicationDate',
            new_name='winter_ApplicationDate',
        ),
    ]
