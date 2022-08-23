"""
Django admin customization.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['email', 'name', 'last_name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name', 'last_name')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'last_name',
                'is_active',
                'is_staff',
                'is_superuser',
            ),
        }),
    )


class StockRequestAdmin(admin.ModelAdmin):
    """Define the admin pages for logs."""
    ordering = ['id']
    list_display = ['symbol', 'user', 'requested_at']
    fieldsets = (
        (None, {'fields': ('symbol', 'user')}),
        (_('Important dates'), {'fields': ('requested_at',)}),
    )
    readonly_fields = ['requested_at']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'symbol',
                'user',
                'requested_at',
            ),
        }),
    )


admin.site.register(models.StockRequest, StockRequestAdmin)
admin.site.register(models.User, UserAdmin)
