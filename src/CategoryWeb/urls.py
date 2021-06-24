"""CategoryWeb URL Configuration. """
from django.urls import include, path

from category.api.base.router import api_urlpatterns as api_v1

urlpatterns = [
    path("api/v1/category-tree/", include(api_v1)),
]
