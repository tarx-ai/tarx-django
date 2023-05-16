from django.contrib import admin
from django.utils.html import mark_safe

from .models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    def get_changeform_initial_data(self, request):
        get_data = super(PostAdmin, self).get_changeform_initial_data(request)
        get_data["author"] = request.user
        return get_data

    list_display = [
        "id",
        "title",
        "author",
        "mins_read",
        "created_at",
    ]

    list_filter = (
        "title",
        "mins_read",
        "created_at",
    )
    search_fields = (
        "title",
        "author",
    )
    ordering = ("created_at",)
    autocomplete_fields = [
        "author",
    ]
    filter_horizontal = [
        "tags",
    ]


class TagAdmin(admin.ModelAdmin):
    # form = TagAdminForm

    list_display = [
        "id",
        "title",
        "background_color",
        "text_color",
        "badge_preview",
    ]

    search_fields = ("title",)

    ordering = ("id",)

    def badge_preview(self, obj):
        # return HTML link that will not be escaped
        return mark_safe(
            f"<div  \
              style='display:flex;justify-content:center;align-items:center;text-align:center;'>  \
            <div style='background-color:{obj.background_color};  \
            padding:10px;   \
            color:{obj.text_color}; \
            border-radius:10px;'>   \
            <h6'>{obj.title}</h6>  \
            </div> \
             </div> \
            "
        )


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
