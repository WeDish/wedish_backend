from django.contrib import admin
from .models import Product, GenericProduct, Service, Unit, Brand, Allergen
from django.utils.translation import gettext_lazy as _

class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class GenericProductAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class ServiceAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class UnitAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('kilograms', 'litre')

class BrandAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description')
    

class AllergenAdmin(admin.ModelAdmin):
    search_fields = ('ALLERGEN_CATEGORIES')

admin.site.register(Product, ProductAdmin)
admin.site.register(GenericProduct, GenericProductAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Brand, BrandAdmin)


