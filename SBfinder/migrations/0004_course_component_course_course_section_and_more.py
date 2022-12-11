# Generated by Django 4.1.1 on 2022-10-19 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SBfinder', '0003_course_subjdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='component',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='course_section',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='meetings',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
