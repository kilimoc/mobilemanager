# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-14 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HouseManager',
            fields=[
                ('id_number', models.IntegerField(max_length=8, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=40)),
                ('phone_number', models.CharField(max_length=14)),
            ],
        ),
    ]
