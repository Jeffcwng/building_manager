# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building_manager', '0005_auto_20141209_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='image',
            field=models.ImageField(default=b'images/apt_default.jpg', null=True, upload_to=b'images', blank=True),
        ),
    ]
