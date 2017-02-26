# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 16:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booker', '0002_auto_20170226_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='ensemble_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booker.Ensemble'),
        ),
    ]
