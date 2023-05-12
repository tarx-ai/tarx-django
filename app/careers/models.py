import uuid

from django.db import models
from django_countries.fields import CountryField


class Profession(models.Model):
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=128, blank=False, default="Developer")

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = "Profession"
        verbose_name_plural = "Professions"


class Vacancy(models.Model):
    JOB_SHIFT = (
        ("Full time", "Full time"),
        ("Part time", "Part time"),
    )

    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)

    profession = models.ForeignKey(Profession, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=64, blank=False)
    description = models.TextField(max_length=1024, blank=True)
    shift = models.CharField(max_length=64, choices=JOB_SHIFT)

    min_salary = models.PositiveIntegerField()
    max_salary = models.PositiveIntegerField()

    country = CountryField(blank=True)
    city = models.CharField(max_length=64, blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"

    def __str__(self) -> str:
        return f"{self.profession}:{self.title}:{self.shift}"
