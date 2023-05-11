from django.db import Error
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.shortcuts import redirect


from .models import AccessRequest, ContactRequest
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


@csrf_protect
def access_request(request):
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == "POST":
        name = request.POST.get("name")
        organization = request.POST.get("organization")
        interest = request.POST.get("interest")
        use_case = request.POST.get("use_case")
        humans_daily = request.POST.get("humans_daily")

        application = AccessRequest.objects.create(
            name=name,
            organization=organization,
            interest=interest,
            use_case=use_case,
            humans_daily=humans_daily,
        )
        try:
            application.save()
        except Error as e:
            logger.error("AccessRequest [%s] not was saved - %s", name, e)
            messages.add_message(
                request,
                messages.ERROR,
                "Error occured while saving the application",
            )
            return redirect("users:access_request")
        logger.info("Access request [%s] saved", name)
        return render(request, "users/thank_you_page.html")
    return render(request, "users/register.html")


def contact(request):
    if request.method == "POST":
        email = request.POST.get("email")
        work_email = request.POST.get("work_email")
        interested_product = request.POST.get("interested_product")
        tarx_plan = request.POST.get("tarx_plan")
        company = request.POST.get("company")
        team_members = request.POST.get("team_members")
        contact = ContactRequest(
            email=email,
            work_email=work_email,
            interested_product=interested_product,
            tarx_plan=tarx_plan,
            company=company,
            team_members=team_members,
        )
        try:
            contact.save()
        except Error as e:
            logger.error(
                "Contact request [%s] - [%s] not was saved\n %s", email, company, e
            )

            return redirect("users:contact")
        logger.info("Contact request [%s] - [%s] saved", email, company)
        return render(request, "users/thank_you_page.html")
    return render(request, "contact/contact_index.html")
