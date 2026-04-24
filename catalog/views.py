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
    context_object_name = "good"
    pk_url_kwarg = "item_id"