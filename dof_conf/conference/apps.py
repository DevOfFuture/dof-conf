from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ConferenceConfig(AppConfig):
    name = 'dof_conf.conference'
    verbose_name = _('Conference')

    def ready(self):
        try:
            import dof_conf.conference.signals  # noqa F401
        except ImportError:
            pass
