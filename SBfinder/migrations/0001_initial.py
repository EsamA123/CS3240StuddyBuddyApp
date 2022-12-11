# Generated by Django 4.1.1 on 2022-10-19 18:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instructor', models.CharField(blank=True, max_length=100, null=True)),
                ('course_number', models.CharField(blank=True, max_length=100, null=True)),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
                ('catalog_number', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('course_section', models.CharField(blank=True, max_length=100, null=True)),
                ('meetings', models.CharField(blank=True, max_length=100, null=True)),
                ('component', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubjData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('user_email', models.EmailField(max_length=254)),
                ('slug', models.SlugField(null=True)),
                ('correspond_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
