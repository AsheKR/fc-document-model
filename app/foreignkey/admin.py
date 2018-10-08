from django.contrib import admin

# Register your models here.
from foreignkey.models import Car, Manufacturer

admin.site.register(Manufacturer)
admin.site.register(Car)