from django.contrib import admin

from .models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "author", "mins_read", "created_at"]

    list_filter = (
        "title",
        "mins_read",
        "created_at",
    )
    search_fields = ("title", "author")
    ordering = ("created_at",)
    autocomplete_fields = ["author"]


admin.site.register(Post, PostAdmin)
