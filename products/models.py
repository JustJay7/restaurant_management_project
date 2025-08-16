from django.db import models

# Existing Item model
class Item(models.Model):
    item_name = models.CharField(max_length=150)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.item_name)


# New Menu model
class Menu(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    items = models.ManyToManyField(Item, related_name="menus")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name