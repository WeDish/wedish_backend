from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import MenuModel, CategoryModel, ManuItemModel


admin.site.register(MenuModel)
admin.site.register(CategoryModel)
admin.site.register(ManuItemModel)