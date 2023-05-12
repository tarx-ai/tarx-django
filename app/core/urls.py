from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # admin
    path("admin/", admin.site.urls),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    # third_party
    path("accounts/", include("allauth.urls")),
    # home views
    path("", views.index, name="index"),
    path("terms", views.terms, name="terms"),
    path("privacy-policy", views.privacy_policy, name="privacy_policy"),
    path("404", views.page_404, name="page_not_found"),
    # logout
    path("logout", views.logout, name="logout"),
    # pricing
    path("pricing", views.pricing, name="pricing"),
    # industry
    path("industry", views.industry, name="industry"),
    # apps urls
    path("", include("users.urls", namespace="users")),
    path("", include("careers.urls", namespace="careers")),
    path("blog", include("blog.urls", namespace="blog")),
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
