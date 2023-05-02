from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # admin
    path("admin/", admin.site.urls),
    # home views
    path("", views.index, name="index"),
    path("terms", views.terms, name="terms"),
    path("privacy-policy", views.privacy_policy, name="privacy_policy"),
    path("404", views.page_404, name="page_not_found"),
    # blog
    path("blog", views.blog, name="blog"),
    path("blog/<int:post_id>", views.blog_details, name="blog_post_details"),
    # careers
    path("careers", views.careers, name="careers"),
    # apps urls
    path("", include("users.urls", namespace="users")),
]
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = (
        [
            path("__debug__/", include(debug_toolbar.urls)),
        ]
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        + urlpatterns
    )

# custom error pages
handler404 = views.handler404
