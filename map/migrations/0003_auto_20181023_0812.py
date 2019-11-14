# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-23 08:12
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_auto_20180914_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forty',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='GID'),
        ),
        migrations.AlterField(
            model_name='forty',
            name='mpoly',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
        ),
    ]