from django.db import models
from tinymce.models import HTMLField
from django.utils.translation import gettext_lazy as _


class Space(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    space_category = models.ForeignKey('SpaceCategory', on_delete=models.SET_NULL, null=True, verbose_name='Space', related_name='spaces')
    accepts_for_production = models.BooleanField(_('Accepts for production'), default=False)
    description = HTMLField(_('Description'), max_length=1000, help_text=_('Short description of this space'))


class SpaceCategory(models.Model):
    name = models.CharField(_('Space Category'), max_length=100)
    description = HTMLField(_('Description'), max_length=1000, help_text=_('Short description of this space category'))


class Table(models.Model):
    public_identifier = models.PositiveIntegerField(_('Public identifier', default=0))
    space = models.ForeignKey(Space, on_delete=models.SET_NULL, null=True, verbose_name='Space', related_name='tables')
    seats_number = models.PositiveIntegerField('Seats number', default=1)

