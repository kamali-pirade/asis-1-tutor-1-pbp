from django.contrib import admin
from django.urls import path

from bookquiz.views import landing_page

urlpatterns = [
    path("admin/", admin.site.urls),
    # TODO [2]: Connect the root URL to the landing page view and name it
    # "landing_page".
]
