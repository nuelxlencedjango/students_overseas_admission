# Generated by Django 4.0.2 on 2022-12-04 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0039_courses_about_courses_detail_courses_overview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='about',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='courses',
            name='detail',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='courses',
            name='overview',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]