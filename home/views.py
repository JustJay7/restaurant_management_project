from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from products.models import Item, Menu
from orders.models import Order
from django.contrib import messages
from decimal import Decimal

def home(request):
    """Homepage of the restaurant management system"""
    menus = Menu.objects.all()
    return render(request, 'home/home.html', {'menus': menus})


def menu_detail(request, menu_id):
    """Display all items in a particular menu"""
    menu = get_object_or_404(Menu, id=menu_id)
    items = menu.items.all()
    return render(request, 'home/menu_detail.html', {'menu': menu, 'items': items})


def create_order(request):
    """
    Create a new order.
    User selects items and quantity from the menu.
    """
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        selected_item_ids = request.POST.getlist('items')
        if not customer_name or not selected_item_ids:
            messages.error(request, "Please provide a customer name and select at least one item.")
            return redirect('create_order')

        order = Order.objects.create(customer_name=customer_name)

        total_price = Decimal('0.00')
        for item_id in selected_item_ids:
            item = get_object_or_404(Item, id=item_id)
            order.items.add(item)
            total_price += item.item_price

        order.total_price = total_price
        order.save()

        messages.success(request, f"Order #{order.id} created successfully!")
        return redirect('order_detail', order_id=order.id)

    items = Item.objects.all()
    return render(request, 'home/create_order.html', {'items': items})


def order_detail(request, order_id):
    """View details of a particular order"""
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'home/order_detail.html', {'order': order})
