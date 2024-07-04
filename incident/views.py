from django.shortcuts import render
from .serializer import IncidentSerializer
from .models  import Incident
from rest_framework.generics import GenericAPIView,UpdateAPIView,RetrieveAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied,NotFound


# Create your views here.
class IncidentApiView(GenericAPIView,ListModelMixin,CreateModelMixin):

    queryset                =       Incident.objects.all()
    serializer_class        =       IncidentSerializer
    authentication_classes  =       [TokenAuthentication,SessionAuthentication]
    permission_classes      =       [IsAuthenticated]

    def get(self,request,*args,**kwargs):
        user=request.user.id
        data=Incident.objects.filter(reporter=user)
        serializer=self.get_serializer(data,many=True,context={'request': request})
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        reporter=request.user.id
        data=request.data
        data['reporter']=reporter
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error":"true"})
        
class UpdateIncidentView(UpdateAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    authentication_classes  =    [TokenAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        incident_id = self.kwargs.get('incident_id')
        incident = Incident.objects.get(incidentId=incident_id)
        if incident.reporter != self.request.user or incident.status == 'closed':
            raise PermissionDenied("You do not have permission to update this incident or This Incident is closed.")
        return incident

    def perform_update(self, serializer):
        serializer.save(reporter=self.request.user)    


class DetailIncidentView(RetrieveAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    authentication_classes  =    [TokenAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        incident_id = self.kwargs.get('incident_id')
        try:
            incident = Incident.objects.get(incidentId=incident_id, reporter=self.request.user)
        except Incident.DoesNotExist:
            raise NotFound("Incident not found or you do not have permission to access it.")
        return incident    


    




