# Generated by Django 4.0.2 on 2022-12-04 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0041_universityaccommodation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='universityaccommodation',
            options={'verbose_name_plural': 'UniversityAccommodation'},
        ),
        migrations.AlterField(
            model_name='universityaccommodation',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='university_accommodation', to='core_app.universities'),
        ),
    ]