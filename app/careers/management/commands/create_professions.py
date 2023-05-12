from django.core.management.base import BaseCommand

from ...models import Profession
from core.logger import logger

PROFESSION_TYPES = ["Design", "Customer Success", "Software Developer"]


class Command(BaseCommand):
    help = "Generate basic professions"

    def handle(self, *args, **options):
        """Generate basic professions"""
        professions = Profession.objects.all()
        if professions:
            return logger.info("Professions already exist")
        for p in PROFESSION_TYPES:
            profession = Profession(title=p)
            profession.save()

        logger.info("%d professions created", Profession.objects.all().count())
