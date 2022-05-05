from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Good, GoodIngradient, VAT


class GoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'recommended_retail_price', 'description', )
    list_display_links = ('name',)
    list_filter = ('category',)
    search_fields = ('name', 'description')


class GoodIngradientAdmin(admin.ModelAdmin):
    list_display = ('good', 'ingradient', 'quantity', 'unit',)
    list_display_links = ('good',)
    list_filter = ('ingradient',)
    search_fields = ('good', 'ingradient')


class VATAdmin(admin.ModelAdmin):
    list_display = ('rate', 'start_date', 'end_date',)


admin.site.register(Good, GoodAdmin)
admin.site.register(GoodIngradient, GoodIngradientAdmin)
admin.site.register(VAT, VATAdmin)    
