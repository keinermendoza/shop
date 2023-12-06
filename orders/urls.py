from django.urls import path 
from django.http import HttpResponse

app_name = "orders"

def no(request):
    return HttpResponse('no')

urlpatterns = [
    path('', no)
]