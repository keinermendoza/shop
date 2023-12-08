from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Address

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email",)

class AddresForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ['user']