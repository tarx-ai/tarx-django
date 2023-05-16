from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post


def blog(request):
    page = request.GET.get("page", 1)

    posts_list = Post.objects.filter(is_active=True).order_by("-created_at").all()
    paginator = Paginator(posts_list, 9)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(
        request,
        "blog/blog_index.html",
        {
            "posts": posts,
            "latest_post": posts_list[0],
        },
    )


def blog_details(request, post_uuid):
    post = get_object_or_404(Post, uuid=post_uuid)
    latest_posts = Post.objects.filter(is_active=True).order_by("-created_at").all()[:3]
    return render(
        request,
        "blog/blog_post_detail.html",
        {
            "post": post,
            "latest_posts": latest_posts,
        },
    )
