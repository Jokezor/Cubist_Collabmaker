from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import *

#@admin.register(User)
#class ShopAdmin(OSMGeoAdmin):
#    list_display = ('first_name', 'gps_location')


# Register your models here.

# User table
admin.site.register(User)

# City table
#admin.site.register(City)

# Skilled people tables
admin.site.register(Passion)
admin.site.register(Assigned_Skill)
admin.site.register(Business_Experience)
admin.site.register(Up_For)

# Colab tables
admin.site.register(Collaboration)
admin.site.register(Colab_Passion)
admin.site.register(Colab_Assigned_Skill)
admin.site.register(Colab_Business_Experience)
admin.site.register(Colab_Up_For)
admin.site.register(Skill)

# Score tables
admin.site.register(Passion_Matched)
admin.site.register(Assigned_Skill_Matched)
admin.site.register(Business_Experience_Matched)
admin.site.register(Up_For_Matched)
admin.site.register(Matched)