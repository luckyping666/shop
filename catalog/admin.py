from django.contrib import admin
from .models import Good

# Register your models here.
@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "currency")
    search_fields = ("name", "description")