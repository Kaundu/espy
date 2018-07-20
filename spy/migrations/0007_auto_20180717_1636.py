# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-17 13:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spy', '0006_image_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='category',
        ),
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.ForeignKey(default=1234, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='spy.Categoryy'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='image',
            name='location',
        ),
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.ForeignKey(default=1234, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='spy.Location'),
            preserve_default=False,
        ),
    ]
