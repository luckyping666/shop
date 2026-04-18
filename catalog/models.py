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