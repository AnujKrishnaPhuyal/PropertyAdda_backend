from rest_framework import serializers
from .models import properties,Usermodel

class property_Serializers(serializers.ModelSerializer):
    class Meta:
        model =properties
        fields = ['id','name','img1','img2','img3','location','type','price','daley_name','daley_number','daley_image','BikeParking','CarParking','AttachedBathroom','Kitchen','Bedroom']

# class UserData_Serializers(serializers.ModelSerializer):
#      class Meta:
#         model =Usermodel
#         fields = ['id','name','email','password','confirmpassword']
