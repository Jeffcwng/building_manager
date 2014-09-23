# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='apt_photo',
            field=models.ImageField(null=True, upload_to=b'images', blank=True),
            preserve_default=True,
        ),
    ]
