# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_sensors_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensors',
            name='test',
        ),
    ]
