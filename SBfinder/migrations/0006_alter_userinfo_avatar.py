# Generated by Django 4.1.1 on 2022-11-28 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SBfinder', '0005_userinfo_major_userinfo_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='avatar',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
