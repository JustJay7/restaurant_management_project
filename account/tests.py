from django.test import TestCase
from products.models import Item
from orders.models import Order  # assuming your Order model is in orders app
from decimal import Decimal

class ItemModelTest(TestCase):
    def setUp(self):
        self.item = Item.objects.create(
            item_name="Margherita Pizza",
            item_price=Decimal('250.00')
        )

    def test_item_creation(self):
        """Test that an item is created correctly"""
        self.assertEqual(self.item.item_name, "Margherita Pizza")
        self.assertEqual(self.item.item_price, Decimal('250.00'))

    def test_item_str_method(self):
        """Test __str__ returns the item name"""
        self.assertEqual(str(self.item), "Margherita Pizza")


class OrderModelTest(TestCase):
    def setUp(self):
        self.item1 = Item.objects.create(item_name="Burger", item_price=Decimal('120.00'))
        self.item2 = Item.objects.create(item_name="Fries", item_price=Decimal('50.00'))

        self.order = Order.objects.create(
            customer_name="John Doe"
        )
        self.order.items.add(self.item1, self.item2)

    def test_order_creation(self):
        """Test order is created correctly with items"""
        self.assertEqual(self.order.customer_name, "John Doe")
        self.assertEqual(self.order.items.count(), 2)

    def test_order_total_calculation(self):
        """Test custom method for calculating total price"""
        # If you have calculate_total() method in Order model
        total = self.order.calculate_total()
        expected_total = Decimal('170.00')  # 120 + 50
        self.assertEqual(total, expected_total)

    def test_order_str_method(self):
        """Test __str__ returns formatted string"""
        self.assertEqual(str(self.order), f"Order {self.order.id} by John Doe")
