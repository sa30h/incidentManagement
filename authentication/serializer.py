from django.db.models import fields
from rest_framework import serializers
from .models import *



class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=['username','email','mobile_number','address','pincode','city','country','password']
        extra_kwargs={
            'password':{'write_only':True}
        }

    def save(self):
        user=User(
            # email=self.validated_data['email'],
            username=self.validated_data['username'],


        )
        password=self.validated_data['password']
        address=self.validated_data['address']
        mobile_number=self.validated_data['mobile_number']
        email=self.validated_data['email']
        pincode=self.validated_data['pincode']
        city=self.validated_data['city']
        country=self.validated_data['country']

        user.address=address
        user.mobile_number=mobile_number
        user.email=email
        user.pincode=pincode
        user.city=city
        user.country=country
        user.set_password(password)
        user.save()
        return user
    
class LoginSerializer(serializers.Serializer):
    # email=serializers.EmailField(max_length=50)
    # username=serializers.CharField(max_length=100)
    # countryCode=serializers.CharField(max_length=100)
    mobile_number=serializers.CharField(max_length=100)
    password=serializers.CharField(max_length=40)