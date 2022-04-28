from django.db import models
from django.utils.translation import gettext_lazy as _
from model.utils import Choices
from model_utils.fields import StatusField
from tinymce.models import HTMLField
from treebeard.mp_tree import MP_Node


UNIT_CATEGORIES = Choices(
            ('kg', _('kilograms')),
            ('L', _('liters')),
            ('pcs', _('units')),
    )

ALLERGEN_CATEGORIES = Choices(
            ('none', _('none')),
            ('celery', _('celery')),
            ('glutten', _('cereals containing glutten')),
            ('crustaceans', _('crustaceans')),
            ('eggs', _('eggs')),
            ('fish', _('fish')),
            ('lupin', _('lupin')),
            ('milk', _('milk')),
            ('molluscs', _('molluscs')),
            ('mustard', _('mustard')),
            ('peanuts', _('peanuts')),
            ('sesame', _('sesame')),
            ('soybeans', _('soybeans')),
            ('SO', _('sulphur dioxide and sulpites > 10 ppm')),
            ('tree nuts', _('tree nuts')),
    )


class Brand(models.Model):
    name = models.CharField(_('name'), max_length=100, null=False, db_index=True)
    picture = models.ImageField(_('picture'), default='wedish_store/img/default_brand.png')
    description = HTMLField(_('description'), max_length=10000, blank=True, default='')
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(_('name'), max_length=100, null=False, db_index=True)
    brand = models.ForeignKey(
        Brand,
        null=False,
        on_delete=models.CASCADE,
        verbose_name=_("brand"),
        related_name='products',
    )
    unit_category = models.CharField(choices=UNIT_CATEGORIES, db_index=True, max_length=7)
    generic_product = models.ForeignKey(
        'GenericProduct',
        null=False,
        on_delete=models.CASCADE,
        verbose_name=_("generic product"),
        related_name='products',
    )

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
        ordering = ['name']
    
    def __str__(self) -> str:
        return f'{self.name}'


class GenericProduct(models.Model):
    name = models.CharField(_('name'), max_length=100, null=False, db_index=True)

    class Meta:
        verbose_name = _('generic product')
        verbose_name_plural = _('generic products')
        ordering = ['name']
    
    def __str__(self) -> str:
        return f'{self.name}'


class ProductAllergen(models.Model):
    name = models.CharField(_('name'), max_length=100, null=False, db_index=True)
    product = models.ForeignKey(
            Product,
            null=True,
            on_delete=models.CASCADE,
            verbose_name=_("product"),
            related_name='allergens',
        )        
    generic_product = models.ForeignKey(
            GenericProduct,
            null=True,
            on_delete=models.CASCADE,
            verbose_name=_("generic groduct"),
            related_name='allergens',
        )

    allergen_category = models.CharField(choices=ALLERGEN_CATEGORIES, db_index=True, max_length=63)

    class Meta:
        verbose_name = _('product allergen')
        verbose_name_plural = _('product allergens')

    def __str__(self) -> str:
        return f'{self.generic_product} {self.product} {self.allergen_category}'


class Service(models.Model):
    name = models.CharField(_('name'), max_length=100)

    class Meta:
        verbose_name = _('service')
        verbose_name_plural = _('services')

    def __str__(self):
        return f'{self.name}'


class Category(MP_Node):
    name = models.CharField(max_length=100)
    
    node_order_by = ['name']

    def __str__(self):
        return 'Category: {}'.format(self.name)
