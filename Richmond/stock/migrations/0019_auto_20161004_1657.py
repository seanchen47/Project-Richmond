# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0018_auto_20161004_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 4, 16, 57, 30, 89435)),
        ),
    ]
