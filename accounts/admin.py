from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email','username', 'last_name', 'first_name', 'age','gender', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age','gender',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age','gender',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
