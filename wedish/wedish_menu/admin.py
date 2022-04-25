from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Menu, Category, MenuItem


admin.site.register(Menu)
admin.site.register(Category)
admin.site.register(MenuItem)