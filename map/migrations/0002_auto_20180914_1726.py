# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-14 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forty',
            name='id_number',
        ),
        migrations.AlterField(
            model_name='forty',
            name='otwarty',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='forty',
            name='zwiedzanie',
            field=models.CharField(max_length=2),
        ),
    ]
