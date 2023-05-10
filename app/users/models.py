import uuid
import os

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.templatetags.static import static


def update_filename(instance, filename):
    return os.path.join(f"uploads/users/{instance.uuid}", filename)


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **other_fields):
        if not email:
            raise ValueError("You must provide an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True.")

        return self.create_user(email, password, **other_fields)


class User(AbstractBaseUser, PermissionsMixin):
    # PROFESSION_CHOICES = (
    #     ("Product Designer", "Product Designer"),
    #     ("UX Designer", "UX Designer"),
    #     ("Frontend Developer", "Engineering Manager"),
    #     ("Frontend Developer", "Frontend Developer"),
    #     ("Backend Developer", "Backend Developer"),
    # )

    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        verbose_name="email address",
        max_length=64,
        blank=False,
        unique=True,
    )
    username = models.CharField(max_length=64, blank=True)
    first_name = models.CharField(max_length=64, blank=True)
    last_name = models.CharField(max_length=64, blank=True)
    avatar = models.ImageField(
        upload_to=update_filename,
        blank=False,
        default=static("assets/image/default_avatar.png"),
    )
    # profession = models.CharField(max_length=64, blank=False, default=) # TODO must be fk on other table

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    objects = UserManager()

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        indexes = [
            models.Index(fields=["uuid", "email"]),
        ]

    def __str__(self) -> str:
        return self.email


class Application(models.Model):
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=64)
    organization = models.CharField(max_length=64)
    interest = models.CharField(max_length=64)
    use_case = models.CharField(max_length=512)
    humans_daily = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.organization}"

    class Meta:
        verbose_name = "application"
        verbose_name_plural = "applications"


class Contact(models.Model):
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)

    email = models.EmailField(max_length=128, blank=False)
    work_email = models.EmailField(max_length=128, blank=False)

    interested_product = models.CharField(max_length=128)
    tarx_plan = models.CharField(max_length=128)
    company = models.CharField(max_length=128, blank=False)
    team_member = models.CharField(max_length=128)
    problems_solve = models.CharField(max_length=1024)

    def __str__(self) -> str:
        return f"{self.email} - {self.company}"
