import stripe
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Good


# Create your views here.
class CatalogView(ListView):
    model = Good
    template_name = "catalog/catalog.html"
    context_object_name = "items"


class GoodDetailView(DetailView):
    model = Good
    template_name = "catalog/item.html"
    context_object_name = "item"
    pk_url_kwarg = "item_id"


def buy_item(request, item_id):
    good = get_object_or_404(Good, id=item_id)
    session = stripe.checkout.Session.create()