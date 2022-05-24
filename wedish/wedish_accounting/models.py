from django.conf import settings
from datetime import date
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from wedish_pub.models import Table
from wedish_menu.models import MenuItem
from wedish_recipy.models import Country


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
    total_price = models.DecimalField(
        _('total price'), null=True, max_digits=10, decimal_places=2, blank=True)

    class Meta:
        ordering = ['table', 'server', 'estimated_to_complete']
        verbose_name = _('order')
        verbose_name_plural = ('orders')
   
    def __str__(self) -> str:
        return str(self.total_price)
    
    @property
    def get_total_price(self):
        self.total_price = 0
        for line in self.places.all():
            self.total_price += line.total_price
        return self.total_price

    def save(self, *args, **kwargs):
        self.get_total_price
        super().save(*args, **kwargs)
        
        
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
        Order,
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

    def save(self, *args, **kwargs):
        self.get_total_price
        super().save(*args, **kwargs)
        self.order.save()


class Bill(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(
        Order,
        on_delete=models.PROTECT,
        null=True,
        verbose_name=_('order'),
        related_name='orders'
    )
    total_price = models.DecimalField(_('total price'), max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    discount =  models.DecimalField(_('discount'), max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    tips =  models.DecimalField(_('tips'), max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    # surinkti pvmus
    
    @property
    def get_total_price(self):
        self.total_price = self.order.total_price - self.discount + self.tips
        return self.total_price

    def save(self, *args, **kwargs):
        self.get_total_price
        super().save(*args, **kwargs)


class Payment(models.Model):
    payment_method = models.CharField(_('payment method'), max_length=100, db_index=True)
    currency = models.CharField(_('currency'), max_length=10, db_index=True)
    bill = models.ForeignKey(Bill, on_delete=models.PROTECT, verbose_name=_('bill'))

    def __str__(self):
        return f'{self.payment_method} @ {self.currency}'


class Company(models.Model):
    company_name = models.CharField(_('company name'), max_length=100, db_index=True, unique=True)
    business_id = models.DecimalField(_('business id'), max_digits=20, decimal_places=0, unique=True, help_text = _('company id'))
    VAT_id = models.CharField(_('VAT id'), max_length=12, db_index=True, unique=True)
    IBAN = models.CharField(_('IBAN'), max_length=34, db_index=True, null=True, blank=True)
    BIC = models.CharField(_('BIC'), max_length=11, null=True, blank=True)
    address = models.CharField(_('address'), max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    email = models.EmailField(_('email'), max_length=150, blank=True, null=True)
    phone_number = PhoneNumberField(_('phone number'), null=True, blank=True)
    is_owner = models.BooleanField(_('is owner'), default=False)

    def __str__(self):
        return f'{self.company_name}'
