from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('register/',views.RegisterApiView.as_view()),
    # path('profile/<id>/',views.RUD_RegisterApi.as_view()),
    path('login/',views.LoginWithTokenAuthenticationAPIView.as_view()),
    # path('otpgenerate/',views.OtpGeneratorAPIView.as_view()),
    # path('otpvalidate/',views.OtpValidation.as_view()),
    # path('logout/',views.User_logout),

]