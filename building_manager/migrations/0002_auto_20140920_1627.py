# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='renter',
            name='smoke',
            field=models.BooleanField(default=False),
        ),
    ]
