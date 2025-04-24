from django.contrib import admin
from .models import UserProfile, EmployeeProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'bio', 'is_active', 'Qualification')

@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'bio', 'created_at')
