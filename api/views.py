from django.shortcuts import render
from .serializers import property_Serializers
# ,UserData_Serializers
from rest_framework.generics import ListAPIView,RetrieveAPIView,ListCreateAPIView
from django.http import JsonResponse
from django.db import IntegrityError
from django.contrib.auth.models import User
from .models import properties,Usermodel
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import json


from django.contrib.auth import login,logout,authenticate


class Property_list(ListAPIView):
    queryset=properties.objects.all()
    serializer_class=property_Serializers

class PropertyDetail(RetrieveAPIView):
    queryset = properties.objects.all()
    serializer_class = property_Serializers
    lookup_field = 'id'  # Specify the field to use for the lookup (in this case, 'id')

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"error": "Property not found"}, status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def create_user_account(request):
    
    if request.method == 'POST':
        try:    
            data=request.body.decode('utf-8')
            user_data = json.loads(data)
            print(user_data)
            signup_data = user_data.get('values')
            print(signup_data)
            if signup_data:
                name = signup_data.get('name')
                email = signup_data.get('email').lower()
                password = signup_data.get('password')
                # if User.objects.filter(email=email).exists():
                #      return JsonResponse({'error': 'Email address already in use'}, status=401)
                # else:
                user = User.objects.create_user(username=name, email=email, password=password)
                user.save()           
                    # return JsonResponse({'message': 'User created successfully'}, status=201)
            return JsonResponse({'message': 'User not found'}, status=400)
        except IntegrityError:
                return JsonResponse({'error': 'Username already exists'}, status=402)

    return JsonResponse({'message': 'data not received'}, status=404)
@csrf_exempt
def login_user(request):
    pass
    if request.method == 'POST':
        try:
            data=request.body.decode('utf-8')
            user_data = json.loads(data)
            Login_data = user_data.get('Login_data')
            if Login_data:
                name = Login_data.get('name').lower()
                password =Login_data.get('password')
                print(name,password)
                user = authenticate(username=name, password=password)
                if user is not None:
                         login(request,user)
                         return JsonResponse({'message': 'User login successfully'}, status=201)
                else:
                    print("user is none")
               
            return JsonResponse({"message":"no logindata "},status=400)
        except:
            return JsonResponse({'error': 'Error in fetching data'}, status=401)
    return JsonResponse({'error': 'request method is not POST request'}, status=410)

    
@csrf_exempt

def create_property(request):
    if request.method == 'POST' :
        try:
            propertyImage1 = request.FILES.get('propertyImage1')
            propertyImage2 = request.FILES.get('propertyImage2')
            propertyImage3 = request.FILES.get('propertyImage3')
            propertyName = request.POST.get('propertyName')
            location = request.POST.get('location')
            propertyType = request.POST.get('propertyType')
            daleyName = request.POST.get('daleyName')
            daleyImage = request.FILES.get('daleyImage')
            daleyPhone = request.POST.get('daleyPhone')
            price = request.POST.get('price')
            bedroom =request.POST.get('Bedroom')
            BikeParking =request.POST.get('BikeParking')
            CarParking =request.POST.get('CarParking')
            AttachedBathroom =request.POST.get('AttachedBathroom')
            Kitchen =request.POST.get('Kitchen')

            
            print(propertyImage1,propertyImage2, propertyImage3, propertyName,location, propertyType,daleyName,daleyImage,daleyPhone,price)
            add_data = properties(img1=propertyImage1,
                                  img2=propertyImage2,
                                  img3=propertyImage3,
                                  name=propertyName,
                                  type=propertyType,
                                  location=location,
                                  price=price,
                                  daley_number=daleyPhone,
                                  daley_name=daleyName,
                                  daley_image=daleyImage,
                                  Bedroom=bedroom,
                                  BikeParking=BikeParking,
                                  CarParking=CarParking,
                                  AttachedBathroom=AttachedBathroom,
                                  Kitchen=Kitchen
                                  )
            add_data.save()
            print(add_data,bedroom,CarParking,BikeParking,AttachedBathroom,Kitchen)
            return JsonResponse({'message': 'Property created successfully'}, status=201)
        except:
            return JsonResponse({'error': 'Error in fetching data'}, status=401)
    return JsonResponse({'error': 'Method not allowed'}, status=405)