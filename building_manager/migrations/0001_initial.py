# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('floor', models.CharField(max_length=20)),
                ('unit_number', models.CharField(max_length=10)),
                ('bedroom', models.PositiveSmallIntegerField()),
                ('bathroom', models.PositiveSmallIntegerField()),
                ('sq_ft', models.PositiveIntegerField()),
                ('rent_amount', models.PositiveIntegerField()),
                ('occupy', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('building_name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=20)),
                ('zip_code', models.IntegerField(max_length=5)),
                ('doorman', models.BooleanField()),
                ('elevator', models.BooleanField()),
                ('pool', models.BooleanField()),
                ('gym', models.BooleanField()),
                ('club_house', models.BooleanField()),
                ('parking', models.CharField(help_text=b'Indoor or Outdoor carport?', max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Renter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=75)),
                ('phone', models.CharField(help_text=b'Format should be: 650-111-2222', max_length=12)),
                ('username', models.CharField(max_length=30)),
                ('age', models.PositiveSmallIntegerField()),
                ('gender', models.CharField(max_length=6)),
                ('has_pet', models.BooleanField()),
                ('smoke', models.BooleanField()),
                ('aptnum', models.OneToOneField(related_name=b'door_number', to='building_manager.Apartment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='apartment',
            name='buidlingnum',
            field=models.ForeignKey(related_name=b'apt_number', to='building_manager.Building'),
            preserve_default=True,
        ),
    ]
