from django.contrib import admin
from . models import *
# Register your models here.

@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ['id','name','number','address1','address2','city','state','zip','order_status_pending','order_status_deliverd','order_status_failed','created']