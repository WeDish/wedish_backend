from django.contrib import admin
from .models import Product, GenericProduct, Service, Brand
from django.utils.translation import gettext_lazy as _


class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class GenericProductAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class ServiceAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    

class BrandAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description')
    

admin.site.register(Product, ProductAdmin)
admin.site.register(GenericProduct, GenericProductAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Brand, BrandAdmin)



