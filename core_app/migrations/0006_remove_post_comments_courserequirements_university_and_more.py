# Generated by Django 4.0.2 on 2022-09-19 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0005_comment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comments',
        ),
        migrations.AddField(
            model_name='courserequirements',
            name='university',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='university', to='core_app.universities'),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
