from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from treebeard.mp_tree import MP_Node


class Menu(models.Model):
    name = models.CharField(_('Name'), max_length=30,
        help_text=_('ex.: Day menu, Festive menu, Ordinary menu'))
    valid_from = models.DateField(_('Valid from'), null=True, blank=True, db_index=True, default=now)
    valid_untill = models.DateField(_('Valid untill'), null=True, blank=True, db_index=True)
    
    PUBLICITY_STATUS = (
        (0, _('Public')),
        (1, _('Private')),
    )

    publicity = models.PositiveIntegerField(_('Publicity'), default=1, choices=PUBLICITY_STATUS)

    class Meta:
        ordering = ['name', 'valid_from']
        verbose_name = _('Menu')
        verbose_name_plural = _('Menus')

    def __str__(self) -> str:
        return f'{self.name} - {self.publicity}'


class Category(MP_Node):
    name = models.CharField(_('Name'), max_length=30,
        help_text=_('ex.: Salad, Roast, Pizza...'))
    node_order_by = ['name']
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True, verbose_name=_('Menu'))

    def __str__(self):
        return 'Category: {}'.format(self.name)


class ManuItem(models.Model):
    name = models.CharField(_('Name'), max_length=30)
    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2, blank=True, null=True)
    category_group = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name=_('Category group'))
    # item = models.ForeignKey(Recipy, on_delete=models.CASCADE, null=True, verbose_name=_('Item'))
