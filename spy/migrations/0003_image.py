# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-12 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spy', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=25)),
                ('category', models.ManyToManyField(to='spy.Category')),
                ('location', models.ManyToManyField(to='spy.Location')),
            ],
        ),
    ]
