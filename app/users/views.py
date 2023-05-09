from django.db import Error
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect, csrf_exempt


from .models import Application
from core.logger import logger


# Create your views here.
@csrf_protect
def login(request):
    if request.method == "POST":
        ...
    return render(request, "users/login.html")


@csrf_exempt
def google_login(request):
    if request.method == "POST":
        ...
    return render(request, "users/login.html")


@csrf_protect
def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        organization = request.POST.get("organization")
        interest = request.POST.get("interest")
        use_case = request.POST.get("use_case")
        humans_daily = request.POST.get("humans_daily")

        application = Application.objects.create(
            name=name,
            organization=organization,
            interest=interest,
            use_case=use_case,
            humans_daily=humans_daily,
        )
        try:
            application.save()
        except Error as e:
            logger.error("Application [%s] not was saved - %s", name, e)
            return render(
                request,
                "users/register.html",
            )
        logger.info("Application [%s] saved", name)
        return render(request, "users/thank_you_page.html")
    return render(request, "users/register.html")
