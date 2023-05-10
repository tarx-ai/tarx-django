import random

from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Post
from users.models import User

fake = Faker()

users = User.objects.all()


class Command(BaseCommand):
    help = "Generate random posts for blog"

    def handle(self, *args, **options):
        for i in range(1, 15):
            post = Post(
                title=fake.name(),
                introduction=fake.sentences(),
                content=fake.text,
                author=random.choice(users),
                mins_read=random.randint(5, 10),
            )
            post.save()
