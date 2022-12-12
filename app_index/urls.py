from django.urls import path
import app_index.views as resource


urlpatterns = [
    path("", resource.HomePage.as_view(), name="index"),
    path("catalogue/", resource.CataloguePage.as_view(), name="catalogue"),
    path("search/", resource.search_view, name="search")
]

