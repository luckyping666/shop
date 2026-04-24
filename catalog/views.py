import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Good, Payment, PaymentStatus


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["STRIPE_PUBLIC_KEY"] = settings.STRIPE_PUBLISH_KEY
        return context


def buy_item(request, item_id):
    good = get_object_or_404(Good, id=item_id)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    session = stripe.checkout.Session.create(
        mode="payment",
        
        line_items=[
            {
                "price_data": {
                    "currency": good.currency,
                    "unit_amount": good.price,
                    "product_data": {
                        "name": good.name,
                        "description": good.desc
                    }
                },
                "quantity": 1
            }
        ],

        success_url=request.build_absolute_uri("/success/"),
        cancel_url=request.build_absolute_uri("/cancel/"),
    )

    payment = Payment(
        good=good,
        session_id=session.id,
        payment_intent=session.payment_intent,
        status=PaymentStatus.PENDING
    )

    payment.save()

    return JsonResponse({"session_id": session.id})
