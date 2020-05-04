from django.contrib import admin
from django.urls import path, include

from client import urls as client_urls
from dashboard import urls as dash_urls

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("dash/", include(dash_urls)),
    path("client/", include(client_urls)),
]
