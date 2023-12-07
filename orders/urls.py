from django import forms 
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        # Obtén el objeto de solicitud del kwargs
        print(kwargs)
        request = kwargs.pop('request')

        # Llama al constructor del formulario
        super(OrderForm, self).__init__(*args, **kwargs)

        if request and request.user.is_authenticated:
            valid_address = request.user.addresses.all()
            print(valid_address)
            self.fields['address_to'].queryset = valid_address # asignando queryset al queryset


from django.shortcuts import render
from django.urls import path 
from django.http import HttpResponse



def no(request):
    return render(request, 'order/no.html', {'form':OrderForm(request=request)})

app_name = "orders"

urlpatterns = [
    path('', no)
]