""" Module Customises Admin views """
# Copied from Code Institute Boutique Ado walkthrough
from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """ Admin Formating for OrderLineItemsinLine """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)

    list_display = ('product',)


class OrderAdmin(admin.ModelAdmin):
    """ Admin Formating for Order """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        'order_number', 'date',
        'order_total', 'original_bag', 'stripe_pid',)

    fields = (
        'order_number', 'user_profile', 'date', 'full_name', 'email',
        'phone_number', 'country', 'postcode', 'town_or_city',
        'street_address_1', 'street_address_2', 'county',
        'order_total', 'original_bag', 'stripe_pid',)

    list_display = (
        'order_number', 'date', 'full_name',
        'order_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
# End Copy
