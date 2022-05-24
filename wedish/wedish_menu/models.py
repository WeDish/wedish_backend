from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from treebeard.mp_tree import MP_Node 
from wedish_recipy.models import Good


class Menu(models.Model):
    name = models.CharField(_('name'), max_length=30,
        help_text=_('ex.: Day menu, Festive menu, Ordinary menu'))
    valid_from = models.DateField(_('valid from'), null=True, blank=True, db_index=True, default=now)
    valid_until = models.DateField(_('valid until'), null=True, blank=True, db_index=True)
    
    PUBLICITY_STATUS = (
        (0, _('Public')),
        (1, _('Private')),
    )

    publicity = models.PositiveIntegerField(_('publicity'), default=1, choices=PUBLICITY_STATUS)

    class Meta:
        ordering = ['name', 'valid_from']
        verbose_name = _('menu')
        verbose_name_plural = _('menus')

    def __str__(self) -> str:
        return f'{self.name} - {self.publicity}'


class Category(MP_Node):
    name = models.CharField(_('name'), max_length=63,
        help_text=_('ex.: Salad, Roast, Pizza...'))
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True, verbose_name=_('menu'))

    node_order_by = ['name']

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return 'Category: {}'.format(self.name)


class MenuItem(models.Model):
    priority_index = models.IntegerField(default=0)
    name = models.CharField(_('name'), max_length=63)
    price = models.DecimalField(_('price'), max_digits=12, decimal_places=2, blank=True, null=True)
    category_group = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name=_('category group'))
    item = models.ForeignKey(Good, on_delete=models.CASCADE, null=True, verbose_name=_('item'))
    net_price = models.DecimalField(_('net price'), max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    vat_amount = models.DecimalField(_('vat amount'), max_digits=10, decimal_places=2, blank=True, null=True, default=0)

    class Meta:
        verbose_name = _('menu item')
        verbose_name_plural = _('menu items')

    @property
    def get_net_price(self):
        if self.item.vat and self.item.vat.rate > 0:
            self.net_price = self.price / (self.item.vat.rate / 100 + 1)
        else:
            self.net_price = self.price
        return self.net_price
    
    @property
    def get_vat_amount(self):
        self.vat_amount = self.price - self.net_price
        return self.vat_amount

    def save(self, *args, **kwargs):
        self.get_net_price
        self.get_vat_amount
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}: {self.price} EUR'
    