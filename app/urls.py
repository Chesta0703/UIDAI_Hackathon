from django.urls import path
from . import views

app_name = "app" 

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('otp/', views.otp, name="otp")
]