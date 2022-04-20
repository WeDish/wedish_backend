from django.db import models
from django.forms import CharField
from django.utils.translation import gettext_lazy as _

class Unit(models.Model):
    UNIT_CATEGORIES = (
            (0, _("kilograms")),
            (1, _("litre")),
    )
    category = models.PositiveIntegerField(_('Unit'), default=0, choices=UNIT_CATEGORIES)

    class Meta:
        verbose_name = _('unit')
        verbose_name_plural = _('units')
    
    def __str__(self) -> str:
        return f'{self.category}'



class Brand(models.Model):
    name = models.CharField(_('name'), max_length=100, null=False, db_index=True)
    picture = models.ImageField(_('picture'), default='wedish_store/img/default_brand.jpg')
    description = CharField(_('description'), max_length=10000, blank=True, default='')
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return f'{self.name}'

class Allergen(models.Model):
    ALLERGEN_CATEGORIES = (
            (0, _("none")),
            (1, _("celery")),
            (2, _("cereals containing glutten")),
            (3, _("crustaceans")),
            (4, _("eggs")),
            (5, _("fish")),
            (6, _("lupin")),
            (7, _("milk")),
            (8, _("molluscs")),
            (9, _("mustard")),
            (10, _("peanuts")),
            (11, _("sesame")),
            (12, _("soybeans")),
            (13, _("sulphur dioxide and sulpites > 10 ppm")),
            (14, _("tree nuts")),
    )
    category = models.PositiveIntegerField(_('Allergen'), default=0, choices=ALLERGEN_CATEGORIES)

    def __str__(self) -> str:
        return f'{self.category}'



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
    #allergen foreign key? example: nuts , eggs, milk, wheat, soy, seafood
    #type foreign key? example: vegan, vegetarian, meat, dairy, glutenfree...


class Service(models.Model):
    name = models.CharField(max_length=100)