from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_id', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_bag', 
                       'stripe_pid',)

    fields = ('order_id', 'user_id', 'full_name', 'email',
              'phone_number', 'town_or_city', 'county',
              'post_code', 'address_line1', 'address_line2',
              'date', 'delivery_cost', 'order_total',
              'grand_total', 'original_bag', 'stripe_pid',)

    list_display = ('order_id', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
