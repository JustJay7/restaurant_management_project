from django.contrib import admin
from .models import Item, Menu

# Custom admin for Item model
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'item_price', 'created_at')
    search_fields = ('item_name',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)

# Custom admin for Menu model
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('menu_name', 'created_at')
    search_fields = ('menu_name',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)
