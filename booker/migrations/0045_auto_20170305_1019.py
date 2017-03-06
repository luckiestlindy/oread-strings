# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 16:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booker', '0044_auto_20170303_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='selectionlist',
            name='bridal',
        ),
        migrations.RemoveField(
            model_name='selectionlist',
            name='communion',
        ),
        migrations.RemoveField(
            model_name='selectionlist',
            name='event',
        ),
        migrations.RemoveField(
            model_name='selectionlist',
            name='prelude_five',
        ),
        migrations.RemoveField(
            model_name='selectionlist',
            name='prelude_four',
        ),
        migrations.RemoveField(
            model_name='selectionlist',
            name='prelude_one',
        ),
        migrations.RemoveField(
            model_name='selectionlist',
            name='prelude_three',
        ),
        migrations.RemoveField(
            model_name='selectionlist',
            name='prelude_two',
        ),
        migrations.RemoveField(
            model_name='selectionlist',
            name='processional',
        ),
        migrations.RemoveField(
            model_name='selectionlist',
            name='recessional',
        ),
        migrations.RemoveField(
            model_name='selectionlist',
            name='unity',
        ),
        migrations.AddField(
            model_name='event',
            name='bridal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bridal', to='booker.Selection'),
        ),
        migrations.AddField(
            model_name='event',
            name='communion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='communion', to='booker.Selection'),
        ),
        migrations.AddField(
            model_name='event',
            name='num_bridesmaids',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='num_flowers',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='num_grandmothers',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='num_mothers',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='num_rings',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='prelude_five',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prelude_five', to='booker.Selection'),
        ),
        migrations.AddField(
            model_name='event',
            name='prelude_four',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prelude_four', to='booker.Selection'),
        ),
        migrations.AddField(
            model_name='event',
            name='prelude_one',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prelude_one', to='booker.Selection'),
        ),
        migrations.AddField(
            model_name='event',
            name='prelude_three',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prelude_three', to='booker.Selection'),
        ),
        migrations.AddField(
            model_name='event',
            name='prelude_two',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prelude_two', to='booker.Selection'),
        ),
        migrations.AddField(
            model_name='event',
            name='processional',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='processional', to='booker.Selection'),
        ),
        migrations.AddField(
            model_name='event',
            name='recessional',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recessional', to='booker.Selection'),
        ),
        migrations.AddField(
            model_name='event',
            name='unity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='unity', to='booker.Selection'),
        ),
        migrations.DeleteModel(
            name='SelectionList',
        ),
    ]