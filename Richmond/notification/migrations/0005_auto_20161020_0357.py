# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0004_auto_20161020_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 20, 3, 57, 10, 795479)),
        ),
    ]