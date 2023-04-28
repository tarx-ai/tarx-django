from django.shortcuts import render


def index(request):
    return render(request, "index.html")


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
