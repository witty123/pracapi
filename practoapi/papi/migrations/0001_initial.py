# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-03 05:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clinics',
            fields=[
                ('clinic_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DiagnosticLabs',
            fields=[
                ('lab_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('doctor_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('qualification', models.TextField()),
                ('specialisation', models.TextField()),
                ('availability', models.CharField(max_length=200)),
                ('clinic', models.ManyToManyField(to='papi.Clinics')),
            ],
        ),
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('test_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=200)),
            ],
        ),
    ]
