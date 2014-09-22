# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, max_length=30, verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')])),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=75, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(help_text=b'Format should be: 650-111-2222', max_length=12)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=(models.Model,),
        ),
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
                ('occupy', models.BooleanField(default=False)),
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
                ('doorman', models.BooleanField(default=False)),
                ('elevator', models.BooleanField(default=False)),
                ('pool', models.BooleanField(default=False)),
                ('gym', models.BooleanField(default=False)),
                ('club_house', models.BooleanField(default=False)),
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
                ('has_pet', models.BooleanField(default=False)),
                ('smoke', models.BooleanField(default=False)),
                ('image', models.ImageField(null=True, upload_to=b'images', blank=True)),
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
