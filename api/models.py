from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

# Create your models here.
class properties(models.Model):
    name = models.CharField(max_length=100)
    img1 = models.ImageField(upload_to='item_images/')
    img2 = models.ImageField(upload_to='item_images/')
    img3 = models.ImageField(upload_to='item_images/')
    location = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    daley_name = models.CharField(max_length=100)
    daley_number = models.CharField(max_length=15)
    daley_image = models.ImageField(upload_to='daley_images/')
    
    def __str__(self):
        return self.name

    

class Usermodel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password =models.CharField(max_length=100)
    confirmpassword =models.CharField(max_length=100)    
    
    def __str__(self):
        return self.email
   
