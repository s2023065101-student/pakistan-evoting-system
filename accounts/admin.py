from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'cnic',
        'full_name',
        'constituency',
        'is_active',
        'is_staff',
    )

    search_fields = (
        'cnic',
        'full_name',
    )

    list_filter = (
        'is_active',
        'is_staff',
    )
