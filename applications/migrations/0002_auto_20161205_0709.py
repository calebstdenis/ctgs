# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-05 07:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 5, 7, 9, 16, 346347)),
        ),
        migrations.AlterField(
            model_name='application',
            name='last_edited',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 5, 7, 9, 16, 346382)),
        ),
    ]
