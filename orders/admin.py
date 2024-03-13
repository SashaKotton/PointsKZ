from django.contrib import admin
from orders.models import Payment, Order, OrderItem

# Register your models here.
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('title', 'total_price')
    list_filter = ('title',)
    search_fields = ('title',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'status', 'deliverer', 'payment', 'comment', 'total_price', 'payment_status',)
    list_filter = ('user_id', 'deliverer', 'payment_status',)
    search_fields = ('user_id', 'status', 'deliverer', 'comment', 'payment_status', )


@admin.register(OrderItem)
class OrderItemAmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'amount', 'order')
    list_filter = ('product', 'amount', 'quantity', 'order')
    search_fields = ('product', 'order')