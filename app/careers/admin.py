from django.contrib import admin

from .models import Vacancy, Profession


class ProfessionAdmin(admin.ModelAdmin):
    model = Profession
    list_display = [
        "id",
        "title",
    ]

    list_filter = ("title",)
    search_fields = ("title",)


class VacancyAdmin(admin.ModelAdmin):
    model = Vacancy
    list_display = [
        "id",
        "profession",
        "title",
        "description",
        "shift",
        "min_salary",
        "max_salary",
        "country",
        "city",
        "created_at",
        "is_active",
    ]

    list_filter = (
        "is_active",
        "min_salary",
        "max_salary",
        "created_at",
    )
    search_fields = ("title",)
    ordering = ("-created_at",)


admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Profession, ProfessionAdmin)
