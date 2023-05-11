from django.contrib import admin

from .models import Vacancy


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
    ]

    list_filter = ()
    search_fields = ()
    ordering = ("created_at",)


admin.site.register(Vacancy, VacancyAdmin)
