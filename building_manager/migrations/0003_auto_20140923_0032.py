# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building_manager', '0002_apartment_apt_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='apt_photo',
            field=models.ImageField(default=b'staticfiles/images/apt_default.jpg', null=True, upload_to=b'images', blank=True),
        ),
        migrations.AlterField(
            model_name='renter',
            name='image',
            field=models.ImageField(default=b'staticfiles/images/renter_default.jpg', null=True, upload_to=b'images', blank=True),
        ),
    ]
