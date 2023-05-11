import uuid

from django.db import models
from django_countries.fields import CountryField


class Vacancy(models.Model):
    JOB_SHIFT = (
        ("FULL TIME", "Full time"),
        ("PART TIME", "Part time"),
    )
    PROFESSION_TYPES = (
        ("DESIGN", "Design"),
        ("CUSTOMER SUCCESS", "Customer Success"),
        ("SOFTWARE DEVELOPER", "Software Developer"),
    )
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    profession = models.CharField(max_length=64, choices=PROFESSION_TYPES)
    title = models.CharField(max_length=64, blank=False)
    description = models.TextField(max_length=1024, blank=True)
    shift = models.CharField(max_length=64, choices=JOB_SHIFT)

    min_salary = models.PositiveIntegerField()
    max_salary = models.PositiveIntegerField()

    country = CountryField(blank=True)
    city = models.CharField(max_length=64, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"

    def __str__(self) -> str:
        return f"{self.profession}:{self.title}:{self.shift}"
