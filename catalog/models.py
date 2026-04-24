from enum import unique
from django.db import models

# Create your models here.
class GoodPriceCurrency(models.TextChoices):
    USD = "usd", "Доллар (США)"
    EUR = "eur", "Евро"
    RUB = "rub", "Российский рубль"


class Good(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название товара"
    )

    desc = models.TextField(
        blank=True,
        verbose_name="Описание товара"
    )

    price = models.PositiveIntegerField(
        verbose_name="Цена (в минимальных единицах)",
        help_text="Цена в копейках/центах"
    )

    currency = models.CharField(
        max_length = 3,
        choices = GoodPriceCurrency.choices,
        default = GoodPriceCurrency.USD,
        verbose_name="Валюта"
    )

    class Meta:
        verbose_name = "Товар",
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


class PaymentStatus(models.TextChoices):
    PENDING = "pending", "Ожидает оплаты"
    PAID = "paid", "Оплачено"
    CANCELED = "canceled", "Отменено"


class Payment(models.Model):
    good = models.ForeignKey(
        "Good",
        on_delete=models.CASCADE,
        related_name="payments",
        verbose_name="Товар"
    )

    session_id = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="ID сессии Stripe"
    )

    payment_intent = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Payment Intent"
    )

    status = models.CharField(
        max_length=20,
        choices=PaymentStatus.choices,
        default=PaymentStatus.PENDING,
        verbose_name="Статус оплаты"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Создано"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Обновлено"
    )

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return f"Платеж №{self.session_id}"
