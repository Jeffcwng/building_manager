from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from models import *
# Register your models here.

admin.site.register(Building)
admin.site.register(Apartment)
admin.site.register(Renter)
admin.site.register(Player, UserAdmin)
# admin.site.register(User)

