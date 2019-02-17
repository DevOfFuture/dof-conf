from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ReservationsConfig(AppConfig):
    name = 'dof_conf.reservations'
    verbose_name = _('Reservations')
