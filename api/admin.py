from django.contrib import admin
from . models import properties,Usermodel
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.

@admin.register(properties)
class propertyAdmin(admin.ModelAdmin):
    list_display=['id','name','img1','img2','img3','location','type','price','daley_name','daley_number','daley_image','BikeParking','CarParking','AttachedBathroom','Kitchen','Bedroom']

@admin.register(Usermodel)
class UsreModelAdmin(admin.ModelAdmin):
    list_display=['id','name','email','password','confirmpassword']


