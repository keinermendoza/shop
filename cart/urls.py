from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
	path('', views.cart_detail, name='cart_detail'),
	# path('cart_edit/<int:product_id>/', views.cart_edit, name='cart_edit'),
	path('add/<int:product_id>/', views.cart_add, name='cart_add'),
	path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
]
