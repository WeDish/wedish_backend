from django.contrib import admin
from .models import Product, GenericProduct, Service, Brand, Category
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from easy_select2 import select2_modelform 


product_item = select2_modelform(Product, attrs={'width': '250px'})


class ProductAdmin(admin.ModelAdmin):
    form = product_item
    list_display = ('name', 'brand', 'unit_category', 'generic_product')
    search_fields = ('name', 'brand__name', 'generic_product__name')
    list_filter = ('name', 'brand', 'generic_product', 'unit_category')


class GenericProductAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class ServiceAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'view_products_link')
    search_fields = ('name', 'description',)
    list_filter = ('name', 'created_at',)

    def view_products_link(self, obj):
        product_count = Product.objects.filter(brand=obj.id).count()
        url = (
            reverse("admin:wedish_store_product_changelist")
            + "?"
            + urlencode({"brand_id": obj.id})
        )
        return format_html('<a href="{}" style="display:block; text-align:center">{}</a>', url, product_count)
    view_products_link.short_description = _('products')


class CategoryAdmin(TreeAdmin):
    form = movenodeform_factory(Category)
    list_filter = ('name',)
    

admin.site.register(Product, ProductAdmin)
admin.site.register(GenericProduct, GenericProductAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
