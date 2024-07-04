from django.db import models
from authentication.models import User
from django.conf import settings
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
# Create your models here.
import random
import datetime

       
class Incident(models.Model):
    priority_choice=(('high','HIGH'),('medium','MEDIUM'),('low','LOW'))
    status_choice=(('open','OPEN'),('inprogress','INPROGRESS'),('closed','CLOSED'))
    type_choice=(('enterprise','ENTERPRISE'),('government','GOVERNMENT'))

    type        =   models.CharField(choices=type_choice,max_length=15,default='ENTERPRISE')
    incidentId =    models.CharField( max_length=15,null=True,default=None,blank=True,unique=True)
    reporter    =   models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    detail      =   models.TextField(max_length=300)
    priority    =   models.CharField(choices=priority_choice,max_length=6,default='HIGH')
    status      =   models.CharField(choices=status_choice,max_length=20,default='OPEN')
    created_at  =   models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.incidentId
    


def check_incident_id_exists(incident_id):
    return Incident.objects.filter(incidentId=incident_id).exists()

def generate_unique_incident_id():
    while True:
        # Generate the Incident ID
        prefix = "RMG"
        random_number = random.randint(10000, 99999)
        current_year = datetime.datetime.now().year
        incident_id = f"{prefix}{random_number}{current_year}"
        
        # Check if the Incident ID already exists
        if not check_incident_id_exists(incident_id):
            return incident_id

def pre_save_incidentId_creator(sender,instance,created,*args,**kwargs):
    
    if created:

        instance.incidentId=generate_unique_incident_id()
        instance.save()
        




post_save.connect(pre_save_incidentId_creator,sender=Incident)


def generate_incident_id(sender, instance, created, **kwargs):
    if created:
        prefix = "RMG"
        random_number = random.randint(10000, 99999)
        current_year = datetime.datetime.now().year
        incident_id = f"{prefix}{random_number}{current_year}"
        instance.incident_id = incident_id
        instance.save()
