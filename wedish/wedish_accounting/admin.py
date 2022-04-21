from django.contrib import admin
from django.utils.translation import gettext as _
from .models import Order, OrderLine, Bill, VAT, Payment

class OrderLineInline(admin.TabularInline):
    model = OrderLine
    fields = ('id', 'order', 'quantity',)
    readonly_fields = ('id',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'server', 'table_number', 'estimated_to_complete', 'price',)
    list_filter = ('estimated_to_complete', 'table_number',)
    search_fields = ('table_number',)
    inlines = (OrderLineInline,)   

class OrderLineAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'quantity',) 
    readonly_fields = ('id',) 
    # fieldsets = (
    #     (None, {
    #         'fields': ('order', 'id', )
    #     }),
    #     (_('Availability'), {
    #         'fields': ()
    #     }),
    # )


class BillAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order', 'total_price', 'discount', 'tips',)
    list_filter = ('customer',)
    search_fields = ('customer', 'order',)

class VATAdmin(admin.ModelAdmin):
    list_display = ('unit_rate', 'start_date', 'end_date',)
      

admin.site.register(Order, OrderLineAdmin)
admin.site.register(OrderLine, OrderLineAdmin)
admin.site.register(Bill, BillAdmin)
admin.site.register(VAT, VATAdmin)      