# Generated by Django 4.1.1 on 2022-11-09 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SBfinder', '0009_alter_study_session_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study_session',
            name='time',
            field=models.TimeField(),
        ),
    ]