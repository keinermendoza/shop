from django.urls import path 
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.registerAddressView, name='register_address')
]
