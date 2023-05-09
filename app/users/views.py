from django.db import Error
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.shortcuts import redirect


from .models import Application
from core.logger import logger


# Create your views here.
@csrf_protect
def login(request):
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        remember_me = request.POST.get("remember_me")
        user = authenticate(email=email, password=password)
        if user is None:
            messages.add_message(
                request,
                messages.ERROR,
                "Bad credentials !",
            )
            logger.error("Bad credentials [%s]", email)
            return redirect("users:login")
        else:
            auth_login(request, user)
            # one time login
            if not remember_me:
                request.session.set_expiry(0)
            logger.info("User has been logged in - [%s]", user)
            return redirect("index")

    return render(request, "users/login.html")


@csrf_exempt
def google_login(request):
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == "POST":
        ...
    return render(request, "users/login.html")


@csrf_protect
def register(request):
    if request.user.is_authenticated:
        return redirect("index")
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
