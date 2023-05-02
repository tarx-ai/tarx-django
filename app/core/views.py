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


def blog(request):
    return render(request, "blog/blog_index.html")


def blog_details(request, post_id):
    return render(request, "blog/blog_post_detail.html")


def careers(request):
    return render(request, "careers/careers_index.html")
