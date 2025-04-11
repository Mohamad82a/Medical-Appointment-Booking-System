from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'is_staff', 'date_joined', 'last_login','last_logout', 'active',)

admin.site.register(User, CustomUserAdmin)