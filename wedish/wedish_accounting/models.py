from django.conf import settings
from datetime import date
from django.db import models
from django.utils.translation import gettext_lazy as _


class Order(models.Model):

    estimated_to_complete = models.DateTimeField(_('Estimated to complete'), null=True, blank=True)
    price = models.CharField(_('Price'), max_length=100, db_index=True)
    completed_at = models.DateTimeField(_('completed_at'), null=True, blank=True, db_index=True)
    table_number = models.CharField(_('Table number'), max_length=100, db_index=True)
    place = models.ForeignKey(
        'Place',
        on_delete=models.CASCADE,
        null=True,
        verbose_name=_('Place'),
        related_name='places',
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    # total_price = total_price (suma visu susijusiu OrderLine) 
    server = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True) #qurysetus admine darytis is staff true

    class Meta:
        ordering = ['table_number', 'server', 'estimated_to_complete']
        verbose_name = _('Order')
        verbose_name_plural = ('Orders')
   
    def __str__(self) -> str:
        return self.price

class OrderLine(models.Model):

    # menu_item = models.ForeignKey('')
    quantity = models.CharField(_('Quantity'), max_length=100)
    # total_price = (on_save menu.menu_item.price * quantity)


class Bill(models.Model):

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(
        'Order',
        on_delete=models.CASCADE,
        null=True,
        verbose_name=_('Order'),
        related_name='orders'
    )
    total_price = models.IntegerField(_('Total price'), db_index=True)
    #surinkti pvmus
    

class VAT(models.Model):

    rate = models.DecimalField(_('Rate'), max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    start_date = models.DateTimeField(_('Start date'), auto_now_add=True)
    end_date = models.DateTimeField(_('End date'), blank=True, null=True )
    # country = country fk i partraukti salis (Countries) is django_cities_light #11 tasko importuota Country
    
    def __str__(self):
        return f'{self.rate} {self.start_date}'

class Payment(models.Model):

    payment_method = models.CharField(_('Payment method'), max_length=100, db_index=True)
    currency = models.CharField(_('Currency'), max_length=10, db_index=True)