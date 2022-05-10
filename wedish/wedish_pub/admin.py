from django.contrib import admin
from .models import SpaceCategory, Space, Table
from django.utils.translation import gettext_lazy as _
from easy_select2 import select2_modelform 

# Register your models here.
space_item = select2_modelform(SpaceCategory, attrs={'width': '250px'})


class SpaceCategoryAdmin(admin.ModelAdmin):
    form = space_item
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    
class SpaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'space_category', 'accepts_for_production',)
    list_display_links = ('name',)
    list_filter = ('space_category',)
    search_fields = ('name',)
    
class TableAdmin(admin.ModelAdmin):
    list_display = ('public_identifier', 'space', 'seats_number',)
    list_display_links = ('public_identifier',)
    list_filter = ('space',)
    search_fields = ('public_identifier',)
    
admin.site.register(SpaceCategory, SpaceCategoryAdmin)
admin.site.register(Space, SpaceAdmin)
admin.site.register(Table, TableAdmin)
