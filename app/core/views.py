from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout

from blog.models import Post
from users.models import FAQ


def index(request):
    latest_posts = Post.objects.filter(is_active=True).order_by("-created_at").all()[:3]
    return render(request, "home/home.html", {"latest_posts": latest_posts})


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


def pricing(request):
    return render(request, "pricing/pricing_index.html")


def industry(request):
    return render(request, "industry/industry_index.html")


def faq(request):
    questions = FAQ.objects.all()
    return render(request, "faq.html", {"questions": questions})
