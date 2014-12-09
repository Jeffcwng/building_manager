# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building_manager', '0003_auto_20140923_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='apt_photo',
            field=models.ImageField(default=b'images/apt_default.jpg', upload_to=b'images'),
        ),
        migrations.AlterField(
            model_name='renter',
            name='image',
            field=models.ImageField(default=b'images/unknown.png', null=True, upload_to=b'images', blank=True),
        ),
    ]
