import os
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from building_project import settings


class Building(models.Model):
    building_name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    zip_code = models.IntegerField(max_length=5)
    doorman = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    gym = models.BooleanField(default=False)
    club_house = models.BooleanField(default=False)
    parking = models.CharField(max_length=30, help_text="Indoor or Outdoor carport?")
    image = models.ImageField(upload_to='images', blank=True, null=True)

    def __unicode__(self):
        return u"{}".format(self.building_name)


class Apartment(models.Model):
    floor = models.CharField(max_length=20)
    unit_number = models.CharField(max_length=10)
    bedroom = models.PositiveSmallIntegerField()
    bathroom = models.PositiveSmallIntegerField()
    sq_ft = models.PositiveIntegerField()
    rent_amount = models.PositiveIntegerField()
    occupy = models.BooleanField(default=False)
    buidlingnum = models.ForeignKey(Building, related_name='apt_number')
    image = models.ImageField(upload_to='images', blank=True, null=True, default='images/apt_default.jpg')

    def __unicode__(self):
        return u"{} - {} floor".format(self.buidlingnum, self.floor)


class Renter(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=12, help_text="Format should be: 650-111-2222")
    username = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=6)
    has_pet = models.BooleanField(default=False)
    smoke = models.BooleanField(default=False)
    aptnum = models.OneToOneField(Apartment, related_name='door_number')
    image = models.ImageField(upload_to='images', blank=True, null=True, default='images/unknown.png')

    def __unicode__(self):
        return u"{}".format(self.username)


class Player(AbstractUser):
    phone = models.CharField(max_length=12, help_text="Format should be: 650-111-2222")

    def __unicode__(self):
        return u"{}".format(self.username)

# class AptImage(models.Model):
#     image = models.ImageField(upload_to='images', blank=True, null=True)
#     apt = models.ForeignKey(Apartment, related_name='photos')