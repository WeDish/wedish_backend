from django.db import models
from django.utils.translation import gettext_lazy as _
from PIL import Image
from tinymce.models import HTMLField
from wedish_store import models as store


# Create your models here.

class Good(models.Model):
    name = models.CharField(_('name'), max_length=50,
                            null=False, db_index=True)
    PRODUCT_CATEGORIES = (
            (0, _("dish")),
            (1, _("drink")),
            (2, _("service")),
    )
    category = models.PositiveIntegerField(
        _('Status'), default=0, choices=PRODUCT_CATEGORIES)
    recommended_retail_price = models.DecimalField(
        _('recommended retail price'), null=False, max_digits=10, decimal_places=2)
    picture = models.ImageField(
        _('picture'), default='wedish_recipy/img/default.jpg')
    description = HTMLField(
        _('description'), max_length=10000, blank=True, default='')
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)


    class Meta:
        verbose_name = _('good')
        verbose_name_plural = _('goods')

    def __str__(self) -> str:
        return f'{self.name} ({self.category}): {self.recommended_retail_price} EUR'
    
class GoodIngradient(models.Model):
    good = models.ForeignKey(
        Good,
        null=False,
        on_delete=models.CASCADE,
        verbose_name=_("good"),
        related_name='ingredients',
    )
    ingradient = models.ForeignKey(
        store.Product,
        null=True,
        on_delete=models.CASCADE,
        verbose_name=_("ingredient"),
        related_name='ingredients',
    )
    quantity = models.DecimalField(
        _('quantity'), null=False, max_digits=10, decimal_places=2, default=0)
    unit = models.ForeignKey(
        store.Unit,
        null=True,
        on_delete=models.CASCADE,
        verbose_name=_("unit"),
        related_name='ingredients',
    )
    
    class Meta:
        verbose_name = _('good ingredient')
        verbose_name_plural = _('good ingredients')

    def __str__(self) -> str:
        return f'{self.good}: {self.ingradient} {self.quantity} EUR'