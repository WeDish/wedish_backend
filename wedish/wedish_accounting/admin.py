from django.contrib import admin
from django.utils.translation import gettext as _
from .models import Order, OrderLine, Bill, VAT, Payment


class OrderLineInline(admin.TabularInline):
    model = OrderLine
    fields = ('id', 'menu_item', 'quantity', 'total_price')
    readonly_fields = ('id','total_price',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'server', 'table', 'estimated_to_complete',)
    list_filter = ('estimated_to_complete', 'table',)
    readonly_fields = ('total_price',)
    # search_fields = ('table',)
    inlines = (OrderLineInline,)   


class OrderLineAdmin(admin.ModelAdmin):
    list_display = ('id', 'menu_item', 'quantity', 'total_price') 
    readonly_fields = ('id','total_price',) 

    fieldsets = (
        ('Standart info', {
            'fields': ('id',)
        }),
        ('Order info', {
            'fields': ('menu_item', 'quantity', 'total_price',)
        }),
    )

class BillAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order', 'total_price', 'discount', 'tips',)
    list_filter = ('customer',)
    search_fields = ('customer', 'order',)


class VATAdmin(admin.ModelAdmin):
    list_display = ('rate', 'start_date', 'end_date',)
      

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine, OrderLineAdmin)
admin.site.register(Bill, BillAdmin)
admin.site.register(VAT, VATAdmin)    
  