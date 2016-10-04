# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cronjob', '0058_auto_20161004_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cron_job_log',
            name='exec_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 4, 20, 13, 22, 363242), verbose_name='cronjob_exec_time'),
        ),
    ]
