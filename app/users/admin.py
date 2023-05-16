# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from allauth.socialaccount.models import SocialAccount, SocialToken

from .models import User, AccessRequest, ContactRequest, FAQ


class MyUserAdmin(UserAdmin):
    model = User

    list_display = (
        "id",
        "uuid",
        "email",
        "profession",
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
            "Base",
            {
                "fields": (
                    "email",
                    "username",
                    "profession",
                    "first_name",
                    "last_name",
                ),
            },
        ),
        (
            "Permissions",
            {
                "fields": ("is_staff", "is_active", "groups"),
            },
        ),
    )
    add_fieldsets = (
        (
            "Base info",
            {
                "fields": (
                    "email",
                    "username",
                    "first_name",
                    "last_name",
                    "profession",
                )
            },
        ),
        (
            "Password",
            {
                "classes": ["wide"],
                "fields": (
                    "password1",
                    "password2",
                ),
            },
        ),
        (
            "Permissions",
            {
                "classes": ["wide"],
                "fields": (
                    "is_superuser",
                    "is_staff",
                    "is_active",
                    "groups",
                ),
            },
        ),
    )
    search_fields = (
        "email",
        "first_name",
        "last_name",
    )
    ordering = ("email",)


class AccessRequestAdmin(admin.ModelAdmin):
    model = AccessRequest
    list_display = (
        "id",
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


class ContactRequestAdmin(admin.ModelAdmin):
    model = ContactRequest
    list_display = (
        "id",
        "email",
        "work_email",
        "interested_product",
        "tarx_plan",
        "company",
        "team_members",
        "solved_problems",
        "is_replied",
        "created_at",
    )
    list_filter = (
        "email",
        "work_email",
        "created_at",
    )
    search_fields = (
        "email",
        "work_email",
    )
    ordering = ("created_at",)


class FAQAdmin(admin.ModelAdmin):
    model = FAQ
    list_display = (
        "id",
        "question",
        "answer",
    )
    list_filter = ("question",)
    search_fields = (
        "question",
        "answer",
    )
    ordering = ("id",)


admin.site.register(User, MyUserAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(AccessRequest, AccessRequestAdmin)
admin.site.register(ContactRequest, ContactRequestAdmin)

# Hiding
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialToken)
