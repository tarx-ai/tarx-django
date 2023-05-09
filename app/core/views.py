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


def blog(request):
    return render(request, "blog/blog_index.html")


def blog_details(request, post_id):
    return render(request, "blog/blog_post_detail.html")


def careers(request):
    return render(request, "careers/careers_index.html")


def contact(request):
    return render(request, "contact/contact_index.html")


def pricing(request):
    return render(request, "pricing/pricing_index.html")
