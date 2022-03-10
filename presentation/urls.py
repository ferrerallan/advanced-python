#from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path, include
from .controllers.HomeView import HomeView
from .controllers.CreateUserView import CreateUserView
from .controllers.TestSerializersView import TestSerializersView

urlpatterns = [
    #   Autenticação
    path('api-auth/', include('rest_framework.urls')),   
    #path('login', obtain_jwt_token),

    #   Home
    path('home/<int:id>', HomeView.as_view()), 

    #   Create User
    path('user', CreateUserView.as_view()), 

    #TestSerializers
    path('testserializers',TestSerializersView.as_view())
]