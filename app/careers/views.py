from django.shortcuts import render

from .models import Vacancy, Profession


def careers(request, location=None):
    vacancies = Vacancy.objects
    location = request.GET.get("location")
    if location:
        vacancies = vacancies.filter(country__name=location)

    professions = Profession.objects.all()
    locations = [vacancy.country.name for vacancy in Vacancy.objects.all()]
    return render(
        request,
        "careers/careers_index.html",
        {
            "vacancies": vacancies.all(),
            "professions": professions,
            "locations": locations,
        },
    )
