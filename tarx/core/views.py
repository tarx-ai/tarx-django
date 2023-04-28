from django.http import HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def terms(request):
    return render(request, "terms.html")


def privacy_policy(request):
    return render(request, "privacy_policy.html")


def handler404(request, *args, **kwargs):
    return HttpResponseNotFound("<h1>Page not found</h1>")
