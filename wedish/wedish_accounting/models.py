from django.conf import settings
from datetime import date
from django.db import models
from django.utils.translation import gettext_lazy as _
from wedish_pub.models import Table
from cities_light.models import AbstractCountry, AbstractCity, AbstractRegion, AbstractSubRegion
from wedish_menu.models import MenuItem


class Country(AbstractCountry):
    pass


class Region(AbstractRegion):
    pass


class SubRegion(AbstractSubRegion):
    pass


class City(AbstractCity):
    pass


class Order(models.Model):
    estimated_to_complete = models.DateTimeField(_('estimated to complete'), null=True, blank=True)
    completed_at = models.DateTimeField(_('completed_at'), null=True, blank=True, db_index=True)
    table = models.ForeignKey(
        Table,
        on_delete=models.CASCADE,
        null=True,
        verbose_name=_('table'),
        related_name='tables',
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='order_for_user')
    server = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='order_for_staff') #qurysetus admine darytis is staff true

    class Meta:
        ordering = ['table', 'server', 'estimated_to_complete']
        verbose_name = _('order')
        verbose_name_plural = ('orders')
   
    def __str__(self) -> str:
        return self.price


class OrderLine(models.Model):
    menu_item = models.ForeignKey(
        MenuItem,
        on_delete=models.CASCADE,
        null=True,
        verbose_name=_('menu item'),
        related_name='menu_items',
    )
    quantity = models.DecimalField(_('quantity'), max_digits=10, decimal_places=3)
    order = models.ForeignKey(
        'Order',
        on_delete=models.CASCADE,
        null=True,
        verbose_name=_('order'),
        related_name='places',
    )
    total_price = models.DecimalField(_('total price'), max_digits=10, decimal_places=2, blank=True, null=True, default=0)
   
    @property
    def get_total_price(self):
        self.total_price = self.menu_item.price * self.quantity
        return self.total_price


class Bill(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(
        'Order',
        on_delete=models.PROTECT,
        null=True,
        verbose_name=_('order'),
        related_name='orders'
    )
    total_price = models.DecimalField(_('total price'), max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    discount =  models.DecimalField(_('discount'), max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    tips =  models.DecimalField(_('tips'), max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    # surinkti pvmus
    

class VAT(models.Model):
    rate = models.DecimalField(_('rate'), max_digits=10, decimal_places=3, blank=True, null=True, default=0)
    start_date = models.DateTimeField(_('start date'), auto_now_add=True)
    end_date = models.DateTimeField(_('end date'), blank=True, null=True )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        null=True,
    )
    
    def __str__(self):
        return f'{self.rate} {self.start_date}'


class Payment(models.Model):
    payment_method = models.CharField(_('payment method'), max_length=100, db_index=True)
    currency = models.CharField(_('currency'), max_length=10, db_index=True)
    bill = models.ForeignKey(Bill, on_delete=models.PROTECT, verbose_name=_('bill'))
