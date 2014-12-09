# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building_manager', '0004_auto_20141209_1835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apartment',
            old_name='apt_photo',
            new_name='image',
        ),
        migrations.AddField(
            model_name='building',
            name='image',
            field=models.ImageField(null=True, upload_to=b'images', blank=True),
            preserve_default=True,
        ),
    ]
