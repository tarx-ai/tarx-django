from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("login", views.login, name="login"),
    path(
        "access_request",
        views.access_request,
        name="access_request",
    ),
    path("contact", views.contact, name="contact"),
]
