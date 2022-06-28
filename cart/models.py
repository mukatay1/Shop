from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    price = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'


class CartItem(models.Model):
    cart = models.ForeignKey(
        'Cart',
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.IntegerField()

    def total_price(self):
        return self.quantity * self.unit_price
