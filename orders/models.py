from django.db import models
from products.models import Item
from django.utils import timezone

class Order(models.Model):
    """
    Represents a customer's order containing multiple items.
    """

    customer_name = models.CharField(max_length=150)
    customer_email = models.EmailField(blank=True, null=True)
    customer_phone = models.CharField(max_length=20, blank=True, null=True)
    shipping_address = models.TextField(blank=True, null=True)

    items = models.ManyToManyField(Item, related_name="orders")

    subtotal_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    shipping_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("PROCESSING", "Processing"),
        ("SHIPPED", "Shipped"),
        ("DELIVERED", "Delivered"),
        ("CANCELLED", "Cancelled"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")

    PAYMENT_METHOD_CHOICES = [
        ("COD", "Cash on Delivery"),
        ("CARD", "Credit/Debit Card"),
        ("UPI", "UPI / Wallets"),
    ]
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default="COD")
    payment_completed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"Order #{self.id} by {self.customer_name}"

    def calculate_subtotal(self):
        """Calculates subtotal by summing all item prices in the order."""
        subtotal = sum(item.price for item in self.items.all())
        self.subtotal_price = subtotal
        return subtotal

    def calculate_total(self):
        """Calculates total price including tax and shipping."""
        subtotal = self.calculate_subtotal()
        self.total_price = subtotal + self.tax_amount + self.shipping_fee
        return self.total_price

    def mark_as_paid(self):
        """Marks the order as paid and updates status."""
        self.payment_completed = True
        self.status = "PROCESSING"
        self.save()

    def mark_as_shipped(self):
        """Updates order status to shipped."""
        self.status = "SHIPPED"
        self.save()

    def mark_as_delivered(self):
        """Updates order status to delivered."""
        self.status = "DELIVERED"
        self.save()

    def cancel_order(self):
        """Cancels the order."""
        self.status = "CANCELLED"
        self.save()
