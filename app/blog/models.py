import uuid
import os

from django.conf import settings
from django.db import models
from colorfield.fields import ColorField
from ckeditor_uploader.fields import RichTextUploadingField


def update_filename(instance, filename):
    return os.path.join(f"uploads/blog/post_{instance.uuid}", filename)


class Post(models.Model):
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=128, blank=False)
    thumbnail = models.ImageField(
        upload_to=update_filename,
        blank=True,
    )
    introduction = models.CharField(max_length=128, blank=False)
    content = RichTextUploadingField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    mins_read = models.IntegerField(default=5)
    is_active = models.BooleanField(default=True)

    # M2M
    tags = models.ManyToManyField("Tag", related_name="posts")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.title[:15]}"

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "post"
        verbose_name_plural = "posts"
        indexes = [
            models.Index(fields=["uuid"]),
        ]


class Tag(models.Model):
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=128, blank=False)
    background_color = ColorField(default="#FF0000", format="hexa")
    text_color = ColorField(default="#000000", format="hexa")

    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "tags"
        ordering = ["-id"]

    def __str__(self) -> str:
        return f"{self.title}"
