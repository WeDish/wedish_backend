from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Menu, Category, MenuItem
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory



class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'valid_from', 'valid_until', 'publicity')
    search_fields = ('name',)
    list_filter = ('valid_from', 'valid_until', 'publicity')


class CategoryAdmin(TreeAdmin):
    form = movenodeform_factory(Category)
    list_filter = ('menu',)


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('priority_index', 'name', 'price', 'category_group', 'item')
    # search_fields = ('name',)
    # list_filter = ('valid_from', 'valid_until', 'publicity')


admin.site.register(Menu, MenuAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(MenuItem, MenuItemAdmin)