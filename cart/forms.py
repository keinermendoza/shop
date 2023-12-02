from django import forms
from django.core.validators import MinValueValidator

# PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    # quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    # quantity = forms.IntegerField(validators=[MinValueValidator(1)])
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'min': 1}), initial=1)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)