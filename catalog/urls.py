from os import name
from django.urls import path
from .views import CatalogView, GoodDetailView, buy_item

app_name = 'catalog'

urlpatterns = [
    path("", CatalogView.as_view(), name="catalog"),
    path("item/<int:item_id>", GoodDetailView.as_view(), name="item_detail"),
    path("buy/<int:item_id>/", buy_item, name="buy_item"),
]