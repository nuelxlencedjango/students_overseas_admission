# Generated by Django 4.0.2 on 2022-10-19 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0017_alter_emergencycontact_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='emergencycontact',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core_app.studentapplication'),
        ),
        migrations.AddField(
            model_name='studentaddress',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core_app.studentapplication'),
        ),
        migrations.AddField(
            model_name='studentpassort',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core_app.studentapplication'),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core_app.studentapplication'),
        ),
    ]
