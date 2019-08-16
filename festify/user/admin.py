from django.contrib import admin
from .models import CustomUser, UserProfile


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'date_joined')
    list_filter = ('is_normaluser', 'is_organization', 'is_staff',)
    search_fields = ('email', 'first_name',)


admin.register(UserProfile)
admin.register(CustomUser)
