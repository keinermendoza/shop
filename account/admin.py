from django.contrib import admin
from .models import User, Address
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ["email", "username", "is_staff", "is_active"]
    list_filter = []


    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "username", "password1", "password2",
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['id' ,'user', 'city']
    search_fields = ['city', 'address', 'postal_code']
