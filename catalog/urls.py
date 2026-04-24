from os import name
from django.urls import path
from .views import CatalogView, GoodDetailView

app_name = 'catalog'

urlpatterns = [
    path("", CatalogView.as_view(), name="catalog"),
    path("item/<int:item_id>", GoodDetailView.as_view(), name="item_detail")
]