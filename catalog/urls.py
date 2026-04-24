from os import name
from django.urls import path
from django.views.generic import TemplateView
from .views import CatalogView, GoodDetailView, buy_item, webhook_view

app_name = 'catalog'

urlpatterns = [
    path("", CatalogView.as_view(), name="catalog"),
    path("item/<int:item_id>", GoodDetailView.as_view(), name="item_detail"),
    
    path("buy/<int:item_id>/", buy_item, name="buy_item"),

    path("success/", TemplateView.as_view(template_name="catalog/success.html"), name="success"),
    path("cancel/", TemplateView.as_view(template_name="catalog/cancel.html"), name="cancel"),

    path("webhook/", webhook_view, name="stripe_webhook"),
]