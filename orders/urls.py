from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('reload-form/', views.get_updated_order_form, name='get_updated_order_form')
]