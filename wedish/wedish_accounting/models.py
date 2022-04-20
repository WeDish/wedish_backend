from django.conf import settings
from datetime import date
from django.db import models
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    quantity = models.CharField(_('Quantity'), max_length=100, db_index=True)
    price = models.CharField(_('Price'), max_length=100, db_index=True)
    completed_at = models.DateTimeField(_('completed_at'), null=True, blank=True, db_index=True)
    table_number = models.CharField(_('Table number'), max_length=100, db_index=True)
    #dish = fk?
    #drinks = fk?

    def __str__(self) -> str:
        return self.price

class Bill(models.Model):
    # payment = fk?
    customer = models.CharField(_('Customer'))#??
    total_price = models.IntegerField(_('Total price'), db_index=True)
    # order = fk?

class VAT(models.Model):
    #country
    rate = models.DecimalField(_('Rate'), max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    start_date = models.DateTimeField(_('Start date'), auto_now_add=True)
    
    def __str__(self):
        return f'{self.rate} {self.start_date}'

class Payment(models.Model):
    payment_method = models.CharField(_('Payment method'), max_length=100, db_index=True)
    currency = models.CharField(_('Currency'), max_length=10, db_index=True)