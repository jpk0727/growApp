# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_sensors_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensors',
            name='lux',
            field=models.FloatField(default=datetime.datetime(2016, 3, 16, 14, 53, 11, 16289, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
