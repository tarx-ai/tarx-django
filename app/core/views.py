from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout


def index(request):
    return render(request, "home/home.html")


def logout(request):
    auth_logout(request)
    return redirect("index")


def terms(request):
    return render(request, "terms.html")


def privacy_policy(request):
    return render(request, "privacy_policy.html")


def page_404(request):
    return render(
        request,
        "404.html",
    )


def handler404(request, *args, **kwargs):
    return render(
        request,
        "404.html",
    )


def careers(request):
    return render(request, "careers/careers_index.html")


def pricing(request):
    return render(request, "pricing/pricing_index.html")


def industry(request):
    return render(request, "industry/industry_index.html")
