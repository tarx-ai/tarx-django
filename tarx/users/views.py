from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "users/index.html")


def login(request):
    return render(request, "users/login.html")


def register(request):
    return render(request, "users/register.html")


def terms(request):
    return render(request, "users/terms.html")


def privacy_policy(request):
    return render(request, "users/privacy_policy.html")
