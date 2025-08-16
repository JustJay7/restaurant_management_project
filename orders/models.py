from django.db import models
from products.models import Item

class Order(models.Model):
    customer_name = models.CharField(max_length=150)
    items = models.ManyToManyField(Item, related_name="orders")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.customer_name}"