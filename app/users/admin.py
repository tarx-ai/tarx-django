# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Application


class UserAdmin(UserAdmin):
    model = User
    list_display = (
        "email",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "email",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            "Permissions",
            {"fields": ("is_staff", "is_active")},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "username",
                    "first_name",
                    "last_name",
                    "password",
                    "is_active",
                    "is_staff",
                )
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


class ApplicationAdmin(admin.ModelAdmin):
    model = Application
    list_display = (
        "name",
        "organization",
        "interest",
        "use_case",
        "humans_daily",
        "created_at",
    )
    list_filter = (
        "name",
        "created_at",
    )
    search_fields = ("name", "organization")
    ordering = ("created_at",)


admin.site.register(User, UserAdmin)
admin.site.register(Application, ApplicationAdmin)
