from datetime import date, timedelta
from django.db import models
from django.utils.translation import gettext_lazy as _
from treebeard.mp_tree import MP_Node


class MenuModel(models.Model):
    name = models.CharField(_('Name'), max_length=30,
        help_text=_('ex.: Day menu, Festive menu, Ordinary menu'))
    valid_from = models.DateField(_('Valid from'), null=True, blank=True, db_index=True, default=date.today())
    valid_untill = models.DateField(_('Valid untill'), null=True, blank=True, db_index=True, default=date.today() + timedelta(days=7))
    
    LOAN_STATUS = (
        (0, _('Public')),
        (1, _('Private')),
    )

    publicity = models.PositiveIntegerField(_('Publicity'), default=1, choices=LOAN_STATUS)

    class Meta:
        ordering = ['name', 'valid_from']
        verbose_name = _('Menu Model')
        verbose_name_plural = _('Menu Models')

    def __str__(self) -> str:
        return f'{self.name} - {self.publicity}'


class CategoryModel(MP_Node):
    name = models.CharField(_('Name'), max_length=30,
        help_text=_('ex.: Salad, Roast, Pizza...'))
    node_order_by = ['name']
    menu = models.ForeignKey(MenuModel, on_delete=models.CASCADE, null=True, verbose_name=_('Menu'))

    def __str__(self):
        return 'Category: {}'.format(self.name)


class ManuItemModel(models.Model):
    name = models.CharField(_('Name'), max_length=30)
    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2, blank=True, null=True)
    category_group = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True, verbose_name=_('Catyegory group'))
    # item = models.ForeignKey(RecipyModel, on_delete=models.CASCADE, null=True, verbose_name=_('Item'))
