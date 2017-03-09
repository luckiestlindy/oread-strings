# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 22:06
from __future__ import unicode_literals

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('booker', '0048_auto_20170306_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '200x300', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
    ]
