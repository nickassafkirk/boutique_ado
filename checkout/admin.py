from django.contrib import admin
from .models import Order, OrderLineItem


# Creates orderline item admin inline to be used within the main order admin panel
# We inherit the admin.TabularInline class
class OrderLineItemAdminInlne(admin.TabularInline):
    # define the model we want to access in admin
    model = OrderLineItem
    # set read_only fields
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    # Allows us to use Orderline item within order admin panel
    inlines = (OrderLineItemAdminInlne,)

    # List fields that are read_only to prevent accidental changes
    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_bag',
                       'stripe_pid')

    # This defines the order of the displayed fields. Otherwise this
    # would be done automatically by django using default order of fields
    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_bag',
                    'stripe_pid')

    # This restricts the fields that appear in the order list to a few key items
    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    # Here we order by date newest to oldest
    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
