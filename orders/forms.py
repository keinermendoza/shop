from django.core.exceptions import ValidationError
from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address_to']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)

        super(OrderCreateForm, self).__init__(*args, **kwargs)

        if self.request and self.request.user.is_authenticated:
            self.fields['address_to'].queryset = self.request.user.addresses.all()



class OrderCreateAdminForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


    def clean(self):
        cleaned_data = super().clean()
        
        # Asegúrate de que los campos 'address_to' y 'user' estén presentes en cleaned_data
        address_to = cleaned_data.get('address_to')
        user = cleaned_data.get('user')

        # if address_to and user:
            # Verifica si la dirección pertenece al usuario
        if address_to not in user.addresses.all():
            raise ValidationError("La dirección debe pertenecer al usuario.")
