from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("nuvemshop_app.urls")),
    path("", include("user_app.urls")),
    path("", include("dashboard_app.urls")),
]


