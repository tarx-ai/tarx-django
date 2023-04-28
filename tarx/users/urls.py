from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("terms", views.register, name="terms"),
    path("privacy-policy", views.register, name="privacy_policy"),
]
