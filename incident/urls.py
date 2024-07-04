from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('incident/', views.IncidentApiView.as_view()),
    path('incident/<str:incident_id>/update/', views.UpdateIncidentView.as_view()),
    path('incident/<str:incident_id>/detail/', views.DetailIncidentView.as_view()),



]