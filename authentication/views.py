from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate,login,get_user_model,logout
from rest_framework import generics,status
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
# from django.contrib.auth import get_user_model
# Create your views here.
# import requests



class RegisterApiView(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=User.objects.all()
    serializer_class=RegisterSerializer
    authentication_classes          =   []
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class RUD_RegisterApi(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset    =User.objects.all()
    serializer_class    = RegisterSerializer
    permission_classes     =   []
    authentication_classes =   []

    lookup_field='id'

    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    
    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)

    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)


class LoginWithTokenAuthenticationAPIView(GenericAPIView):
    queryset= User.objects.all()
    serializer_class    =       LoginSerializer
    permission_classes     =   []
    authentication_classes =   []

    def post(self,request):
        mobile_number    =   request.data.get('mobile_number')
        password    =   request.data.get('password')
        print('mobileno',mobile_number,'pass',password)
        # user        =   User.objects.get(email=str(email))
        verify_mobile_no = User.objects.filter(mobile_number=mobile_number)
        print('verify',verify_mobile_no)
        if not verify_mobile_no:
            print("yesyes",verify_mobile_no)
            response = {
			"data": {
				"message": "Your login information is invalid",
				"status": "invalid"
			}
		}
            return Response(response)
        user          =   authenticate(mobile_number=mobile_number,password=password)
        print('user',user)
        if user is not None:
            # login(user,request)
            #TOKEN STUFF
            token, _ = Token.objects.get_or_create(user = user)
            login(request,user)
            print('user not none',token)
            #token_expire_handler will check, if the token is expired it will generate new one
            # is_expired, token = token_expire_handler(token)     # The implementation will be described further

            return Response({ 
                'token': token.key,
                'id':user.id,
            } )
        response = {
        "data": {
            "message": "Your login information is invalid",
            "status": "invalid"
        }
    }
        return Response(response)
