from django.urls import path

from . import views


app_name = "blog"

urlpatterns = [
    path("", views.blog, name="index"),
    path("<str:post_uuid>", views.blog_details, name="post_details"),
]
