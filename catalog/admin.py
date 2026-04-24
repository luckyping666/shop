from django.contrib import admin
from .models import Good, Payment

# Register your models here.
@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "currency")
    search_fields = ("name", "description")


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "good", "status", "session_id", "created_at")
    search_fields = ("session_id", "payment_intent")