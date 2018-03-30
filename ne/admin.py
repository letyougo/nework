from django.contrib import admin

# Register your models here.

from .models import *

class profile_admin(admin.ModelAdmin):
    list_display = ('nickname','address','sex')
admin.site.register(Profile,profile_admin)

class auth_admin(admin.ModelAdmin):
    list_display = ('profile','type','key','value','checked')

admin.site.register(Auth,auth_admin)

class demand_type_admin(admin.ModelAdmin):
    list_display = ('name','deleted')

class deman_admin(admin.ModelAdmin):
    list_display = ('user','type','title','dead_line','budget','deleted')

admin.site.register(DemandType)
admin.site.register(Demand,deman_admin)