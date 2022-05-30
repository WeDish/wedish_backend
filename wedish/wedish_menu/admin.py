from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from easy_select2 import select2_modelform 
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from .models import Menu, Category, MenuItem


menu_item = select2_modelform(MenuItem, attrs={'width': '250px'})

class MenuItemInline(admin.TabularInline):
    model = MenuItem
    form = menu_item
    show_change_link = True
    exclude = ['net_price', 'vat_amount']

    class Media:
        js = (
            '/static/js/get_wedish_recipy_goods_values.js',
        )


class CategoryInline(admin.TabularInline):
    model = Category
    show_change_link = True

class MenuItemInline(admin.TabularInline):
    model = MenuItem
    form = menu_item
    show_change_link = True
    exclude = ['net_price', 'vat_amount']

    class Media:
        js = (
            '/static/js/get_wedish_recipy_goods_values.js',
        )


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'valid_from', 'valid_until', 'publicity')
    search_fields = ('name',)
    list_filter = ('valid_from', 'valid_until', 'publicity')
    inlines = (CategoryInline,)


class CategoryAdmin(TreeAdmin):
    list_display = ('name', 'menu',)
    form = movenodeform_factory(Category)
    list_filter = ('menu',)
    inlines = (MenuItemInline,)


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('priority_index', 'name', 'price', 'net_price', 'vat_amount', 'category_group', 'item')
    list_display_links = ('name', )
    readonly_fields = ('category_group',)

    def has_add_permission(self, request, obj=None):
        return False


admin.site.register(Menu, MenuAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
