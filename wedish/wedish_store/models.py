from unicodedata import category
from django.db import models
from django.forms import CharField
from django.utils.translation import gettext_lazy as _
from model_utils import Choices

class Unit(models.Model):
    UNIT_CATEGORIES = Choices(
            (0, 'kilograms', _('kilograms')),
            (1, 'litres', _('litres')),
    )
    unit_category = models.PositiveSmallIntegerField(
        choices=UNIT_CATEGORIES,
        default=UNIT_CATEGORIES.kilograms)

    class Meta:
        verbose_name = _('unit')
        verbose_name_plural = _('units')
    
    def __str__(self) -> str:
        return f'{self.unit_category}'



class Brand(models.Model):
    name = models.CharField(_('name'), max_length=100, null=False, db_index=True)
    picture = models.ImageField(_('picture'), default='wedish_store/img/default_brand.png')
    description = CharField(_('description'), max_length=10000, blank=True, default='')
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return f'{self.name}'

class Allergen(models.Model):
    ALLERGEN_CATEGORIES = Choices(
            ('non', _('none')),
            ('cel', _('celery')),
            ('glut', _('cereals containing glutten')),
            ('crust', _('crustaceans')),
            ('egg', _('eggs')),
            ('fish', _('fish')),
            ('lup', _('lupin')),
            ('mlk', _('milk')),
            ('mlsc', _('molluscs')),
            ('must', _('mustard')),
            ('pnut', _('peanuts')),
            ('ssme', _('sesame')),
            ('soy', _('soybeans')),
            ('SO', _('sulphur dioxide and sulpites > 10 ppm')),
            ('tnut', _('tree nuts')),
    )
    allergen_category = models.CharField(
        max_length=32,
        choices = ALLERGEN_CATEGORIES,
        default = ALLERGEN_CATEGORIES.non
    )

    def __str__(self) -> str:
        return f'{self.allergen_category}'



class Product(models.Model):
    name = models.CharField(_('Name'), max_length=100, null=False, db_index=True)
    unit_rate = models.DecimalField(_('Unit Rate'), null=False, max_digits=10, decimal_places=2, default=0, help_text=_("Ration between generic_product.unit and unit"))
    brand = models.ForeignKey(
        Brand,
        null=False,
        on_delete=models.CASCADE,
        verbose_name=_("Brand"),
        related_name='products',
    )
    unit = models.ForeignKey(
        Unit,
        null=False,
        on_delete=models.CASCADE,
        verbose_name=_("Unit"),
        related_name='products',
    )
    generic_product = models.ForeignKey(
        'Generic Product',
        null=False,
        on_delete=models.CASCADE,
        verbose_name=_("Generic Product"),
        related_name='products',
    )

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        ordering = ['name']



class GenericProduct(models.Model):
    name = models.CharField(_('Name'), max_length=100, null=False, db_index=True)
    product = models.ForeignKey(
        Product,
        null=True,
        on_delete=models.CASCADE,
        verbose_name=_("Product"),
        related_name='generics',
    )
    allergen = models.ForeignKey(
        Allergen,
        null=True,
        on_delete=models.CASCADE,
        verbose_name=_("Allergen"),
        related_name='generics',
    )
    
    class Meta:
        verbose_name = _('generic product')
        verbose_name_plural = _('generic products')
        ordering = ['name']
    
    def __str__(self) -> str:
        return f'{self.product} {self.allergen}'

class Service(models.Model):
    name = models.CharField(max_length=100)