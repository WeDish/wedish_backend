from django.db import models
from tinymce.models import HTMLField
from django.utils.translation import gettext_lazy as _


class SpaceCategory(models.Model):
    name = models.CharField(_('space category'), max_length=100)
    description = HTMLField(_('description'), max_length=1000, help_text=_('Short description of this space category'))

    class Meta:
        verbose_name = _('space category')
        verbose_name_plural = _('space categories')

    def __str__(self) -> str:
        return str({self.name})


class Space(models.Model):
    name = models.CharField(_('name'), max_length=100)
    space_category = models.ForeignKey(SpaceCategory, on_delete=models.SET_NULL, null=True, verbose_name='space', related_name='spaces')
    accepts_for_production = models.BooleanField(_('accepts for production'), default=False)
    description = HTMLField(_('description'), max_length=1000, help_text=_('Short description of this space'))

    class Meta:
        verbose_name = _('space')
        verbose_name_plural = _('spaces')

    def __str__(self) -> str:
        return f'{self.name} - {self.space_category}'


class Table(models.Model):
    public_identifier = models.PositiveIntegerField(_('public identifier'), default=0)
    space = models.ForeignKey(Space, on_delete=models.SET_NULL, null=True, verbose_name='space', related_name='tables')
    seats_number = models.PositiveIntegerField('seats number', default=1)
    occupied = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('table')
        verbose_name_plural = _('tables')

    def __str__(self) -> str:
        return f'{self.space}:{self.seats_number}'
