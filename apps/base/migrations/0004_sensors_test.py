# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_sensors_java_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensors',
            name='test',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
