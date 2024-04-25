
from django.urls import path
from api import views
# from .views import create_user

urlpatterns = [
    path('property/',views.Property_list.as_view()),
     path('property/<int:id>/', views.PropertyDetail.as_view(), name='property-detail'),
     path('create_user_account/', views.create_user_account, name='create_user_account'),
     path('login_user/', views.login_user, name='login_user'),
     path('create_property/', views.create_property, name='create_property'),


]