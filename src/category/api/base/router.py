from django.contrib import admin
from django.urls import path

from category.api.base.categories import CategoryListView
from category.api.base.category import CategoryDetailView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("categories/", CategoryListView.as_view()),
    path("categories/<int:category_id>", CategoryDetailView.as_view()),
]


api_urlpatterns = urlpatterns
