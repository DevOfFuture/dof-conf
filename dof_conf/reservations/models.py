from django.db import models
from django.utils.translation import ugettext_lazy as _

from dof_conf.core.models import BaseModel


class Reservation(BaseModel):
    """
    Stores info about a single person who reserved a spot at the conference.
    """
    name = models.CharField(_('name'), max_length=100)
    email = models.EmailField(_('email address'), max_length=254, unique=True)
    number_of_tees = models.PositiveSmallIntegerField(
        _('number of tees'),
        help_text=_('The number of T-Shirts we should save for you.'),
        default=1
    )
    number_of_stickers = models.PositiveSmallIntegerField(
        _('number of stickers'),
        help_text=_('The number of stickers we should save for you.'),
        default=1
    )
    subscribed = models.BooleanField(
        _('subscribed'),
        help_text=_('Designates whether the person has subscribed to news about '
                    'the event.'),
        default=True
    )

    class Meta:
        verbose_name = _('reservation')
        verbose_name_plural = _('reservations')
        ordering = ('created',)

    def __str__(self):
        return self.name
