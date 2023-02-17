from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework import permissions, authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import GenericAPIView
from .serializers import *
from ..models import *





class mid_level_user_register(GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = Mid_level_UserSerializer
    def post(self, request):
        first_name = request.data['first_name']
        last_name = request.data['last_name'] 
        phone_number = request.data['phone_number']
        email = request.data['email']
        password = request.data['password']
        address = request.data['address']
        Is_user = User.objects.filter(username=phone_number).exists()
        if Is_user:
            response={
                "message" : 'Already Registered!',
            }
        else:
            user = User.objects.create_user(phone_number, email, password)
            user_info=Mid_level_User.objects.create(first_name=first_name,last_name=last_name,phone_number=phone_number,address=address,email=email,user=user)
            
            user.is_active=True
            user.is_midlevel=True
            user.save()
            refresh = RefreshToken.for_user(user)
            if user_info is not None:
                user_serializer=Mid_level_UserSerializer(user_info)
                response={
                    "result" : user_serializer.data,
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    "message" : 'Registered Successfully',
                    "status" : 1
                }
            else:
                response={
                    "message" : 'Sorry, something went wrong !',
                    "status" : 0
                }
        return Response(response)


class low_level_user_register(GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = Low_level_UserSerializer
    def post(self, request):
        first_name = request.data['first_name']
        last_name = request.data['last_name'] 
        phone_number = request.data['phone_number']
        email = request.data['email']
        password = request.data['password']
        address = request.data['address']
        Is_user = User.objects.filter(username=phone_number,email=email)
        if Is_user.exists():
            response={
                "message" : 'Already Registered!',
            }
        else:
            user = User.objects.create_user(phone_number, email, password)
            user_info=Low_level_User.objects.create(first_name=first_name,last_name=last_name,phone_number=phone_number,address=address,email=email,user=user)
            user.is_active=True
            user.is_lowlevel=True
            user.save()
            refresh = RefreshToken.for_user(user)
            if user_info is not None:
                user_serializer=Low_level_UserSerializer(user_info)
                response={
                    "result" : user_serializer.data,
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    "message" : 'Registered Successfully',
                    "status" : 1
                }
            else:
                response={
                    "message" : 'Sorry, something went wrong !',
                    "status" : 0
                }
        return Response(response)



class high_level_user_register(GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = High_level_UserSerializer
    def post(self, request):
        first_name = request.data['first_name']
        last_name = request.data['last_name'] 
        phone_number = request.data['phone_number']
        email = request.data['email']
        password = request.data['password']
        address = request.data['address']
        Is_user = User.objects.filter(username=phone_number).exists()
        if Is_user:
            response={
                "message" : 'Already Registered!',
            }
        else:
            user = User.objects.create_user(phone_number, email, password)
            user_info=High_level_User.objects.create(first_name=first_name,last_name=last_name,phone_number=phone_number,address=address,email=email,user=user)
            user.is_active=True
            user.is_highlevel=True
            user.save()
            refresh = RefreshToken.for_user(user)
            if user_info is not None:
                user_serializer=High_level_UserSerializer(user_info)
                response={
                    "result" : user_serializer.data,
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    "message" : 'Registered Successfully',
                    "status" : 1
                }
            else:
                response={
                    "message" : 'Sorry, something went wrong !',
                    "status" : 0
                }
        return Response(response)

class LoginView(GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LoginSerializer


    def post(self, request):
        phone_number = request.data.get("phone_number")
        password = request.data.get("password")
        if phone_number is None or password is None:
            return Response({'error': 'Please provide both username and password'})
        user = authenticate(username=phone_number, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'})
        serializer = UserSerializer(user)
        return Response({ 
            "message" : 'Success',
            "serializer": serializer.data})
        
