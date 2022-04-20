from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Product, GenericProduct, Service, Unit, Brand


admin.site.register(Product, GenericProduct, Service, Unit, Brand)



