from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from easy_select2 import select2_modelform 
from .models import Good, GoodIngradient


good_item = select2_modelform(Good, attrs={'width': '250px'})


class GoodAdmin(admin.ModelAdmin):
    form = good_item
    list_display = ('name', 'category', 'recommended_retail_price', 'description',)
    list_display_links = ('name',)
    list_filter = ('category',)
    search_fields = ('name', 'description')


class GoodIngradientAdmin(admin.ModelAdmin):
    list_display = ('good', 'ingradient', 'quantity', 'unit',)
    list_display_links = ('good',)
    list_filter = ('ingradient',)
    search_fields = ('good', 'ingradient')
    

admin.site.register(Good, GoodAdmin)
admin.site.register(GoodIngradient, GoodIngradientAdmin)
