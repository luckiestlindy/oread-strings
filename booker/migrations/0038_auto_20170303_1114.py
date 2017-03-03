# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 17:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booker', '0037_auto_20170303_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='selectionlist',
            name='prelude_five',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prelude_five', to='booker.Selection'),
        ),
        migrations.AddField(
            model_name='selectionlist',
            name='prelude_four',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prelude_four', to='booker.Selection'),
        ),
        migrations.AddField(
            model_name='selectionlist',
            name='prelude_one',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prelude_one', to='booker.Selection'),
        ),
        migrations.AddField(
            model_name='selectionlist',
            name='prelude_three',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prelude_three', to='booker.Selection'),
        ),
        migrations.AddField(
            model_name='selectionlist',
            name='prelude_two',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prelude_two', to='booker.Selection'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_outdoors',
            field=models.CharField(choices=[('Not Sure Yet', 'Not Sure Yet'), ('Yes', 'Yes'), ('No', 'No')], default='1', max_length=20),
        ),
    ]