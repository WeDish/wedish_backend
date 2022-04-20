from django.contrib import admin
<<<<<<< Updated upstream
from django.utils.translation import gettext_lazy as _
from .models import Product, GenericProduct, Service, Unit, Brand


admin.site.register(Product, GenericProduct, Service, Unit, Brand)


=======
from .models import Product, GenericProduct, Service, Unit, Brand
from django.utils.translation import gettext_lazy as _

class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class GenericProductAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class ServiceAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class UnitAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class BrandAdmin(admin.ModelAdmin):
    search_fields = ('name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(GenericProduct, GenericProductAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Brand, BrandAdmin)
>>>>>>> Stashed changes

