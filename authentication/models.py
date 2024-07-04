
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



class User(AbstractUser):
    mobile_number        =   models.CharField(max_length=11,unique=True)
    address              =   models.TextField(max_length=250)
    pincode              =   models.CharField(max_length=6)
    city                 =   models.CharField(max_length=50)
    country              =   models.CharField(max_length=50)

    @property
    def owner(self):
        return self.user

    
    USERNAME_FIELD = 'mobile_number'
    REQUIRED_FIELDS = ["username"]



@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)