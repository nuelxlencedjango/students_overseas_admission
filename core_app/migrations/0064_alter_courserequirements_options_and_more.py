# Generated by Django 4.0.2 on 2023-02-05 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0063_workexperience_emergencycontact'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courserequirements',
            options={'verbose_name_plural': 'Course Requirements'},
        ),
        migrations.AlterModelOptions(
            name='courseselection',
            options={'verbose_name_plural': 'Course Selection'},
        ),
        migrations.AlterModelOptions(
            name='universityaccommodation',
            options={'verbose_name_plural': 'University Accommodation'},
        ),
        migrations.AlterModelOptions(
            name='universityimages',
            options={'verbose_name_plural': 'University Images'},
        ),
    ]