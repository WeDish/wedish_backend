from django.contrib import admin
from .models import Good, GoodIngradient
from django.utils.translation import gettext_lazy as _

# Register your models here.

class GoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'recommended_retail_price', 'description',)
    list_display_links = ('name',)
    list_filter = ('category',)
    search_fields = ('name', 'description')
    
class GoodIngradientAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Good, GoodAdmin)
admin.site.register(GoodIngradient, GoodIngradientAdmin)
admin.site.site_title = _('wedish recipy admin')
admin.site.site_header = _('wedish recipy administration')

