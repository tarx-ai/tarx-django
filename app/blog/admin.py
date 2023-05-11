from django.contrib import admin

from .models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    def get_changeform_initial_data(self, request):
        get_data = super(PostAdmin, self).get_changeform_initial_data(request)
        get_data["author"] = request.user
        return get_data

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
