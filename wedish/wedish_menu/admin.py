from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from easy_select2 import select2_modelform
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from .models import Menu, Category, MenuItem


menu_item = select2_modelform(MenuItem, attrs={'width': '250px'})


class MenuItemLineInline(admin.TabularInline):
    model = MenuItem
    form = menu_item
    show_change_link = True


class CategoryLineInline(admin.TabularInline):
    model = Category
    show_change_link = True


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'valid_from', 'valid_until', 'publicity')
    search_fields = ('name',)
    list_filter = ('valid_from', 'valid_until', 'publicity')
    inlines = (CategoryLineInline,)


class CategoryAdmin(TreeAdmin):
    list_display = ('name', 'menu',)
    form = movenodeform_factory(Category)
    list_filter = ('menu',)
    inlines = (MenuItemLineInline,)


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('priority_index', 'name', 'price', 'category_group', 'item')
    list_display_links = ('name', )
    readonly_fields = ('category_group',)

    def has_add_permission(self, request, obj=None):
        return False


admin.site.register(Menu, MenuAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.site_title = _('wedish menu admin')
admin.site.site_header = _('wedish menu administration')
