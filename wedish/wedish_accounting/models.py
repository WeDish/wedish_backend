from django.conf import settings
from datetime import date
from django.db import models
from django.utils.translation import gettext_lazy as _
from wedish_pub.models import Table
from cities_light.models import Country
from wedish_menu.models import MenuItem


class Order(models.Model):

    estimated_to_complete = models.DateTimeField(_('Estimated to complete'), null=True, blank=True)
    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    completed_at = models.DateTimeField(_('completed_at'), null=True, blank=True, db_index=True)
    table = models.ForeignKey(
        Table,
        on_delete=models.CASCADE,
        null=True,
        verbose_name=_('table'),
        related_name='tables',
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='order_for_user')
    # total_price = total_price (suma visu susijusiu OrderLine) 
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
    quantity = models.CharField(_('Quantity'), max_length=100)
    order = models.ForeignKey(
        'Order',
        on_delete=models.CASCADE,
        null=True,
        verbose_name=_('order'),
        related_name='places',
    )
    total_price = models.DecimalField(_('Total price'), max_digits=10, decimal_places=2, blank=True, null=True, default=0)
   
    @property
    def get_total_price(self):
       total_price = self.menu_item.price * self.quantity
       return total_price



class Bill(models.Model):

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(
        'Order',
        on_delete=models.PROTECT,
        null=True,
        verbose_name=_('order'),
        related_name='orders'
    )

    total_price = models.DecimalField(_('Total price'), max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    discount =  models.DecimalField(_('Discount'), max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    tips =  models.DecimalField(_('Tips'), max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    # surinkti pvmus
    

class VAT(models.Model):
    rate = models.DecimalField(_('Rate'), max_digits=10, decimal_places=3, blank=True, null=True, default=0)
    start_date = models.DateTimeField(_('Start date'), auto_now_add=True)
    end_date = models.DateTimeField(_('End date'), blank=True, null=True )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        null=True,
    )
    # country fk i partraukti salis (Countries) is django_cities_light #11 tasko importuota Country
    
    def __str__(self):
        return f'{self.rate} {self.start_date}'


class Payment(models.Model):

    payment_method = models.CharField(_('Payment method'), max_length=100, db_index=True)
    currency = models.CharField(_('Currency'), max_length=10, db_index=True)