from django.db import models
from django.utils.translation import ugettext_lazy as _

from dof_conf.core.models import BaseModel
from dof_conf.utils.storage import upload_to


class Speaker(BaseModel):
    """
    Stores info of a single speaker of the conference.
    """
    name = models.CharField(_('name'), max_length=100, unique=True)
    about = models.TextField(_('about'), blank=True)
    github = models.URLField(_('GitHub'), blank=True)
    facebook = models.URLField(_('Facebook'), blank=True)
    twitter = models.URLField(_('Twitter'), blank=True)
    linkedin = models.URLField(_('LinkedIn'), blank=True)
    photo = models.ImageField(_('photo'), upload_to=upload_to, blank=True)
    position = models.PositiveIntegerField(
        _('position'),
        default=1,
        help_text=_('Determines at which position this speaker is displayed '
                    'on the website.')
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_('Designates whether this speaker should be treated as '
                    'active or not. Unselect this instead of deleting speakers.')
    )

    class Meta:
        verbose_name = _('speaker')
        verbose_name_plural = _('speakers')
        ordering = ('position',)

    def __str__(self):
        return self.name


class ScheduleItem(BaseModel):
    """
    Stores info about an activity during the conf. Might be a talk, a workshop,
    a live coding session...
    """
    speaker = models.ForeignKey(
        Speaker,
        on_delete=models.CASCADE,
        verbose_name=_('speaker'),
        related_name='appearances',
        null=True,
        blank=True
    )
    title = models.CharField(_('title'), max_length=200)
    datetime = models.DateTimeField(_('date and time'))
    about = models.TextField(_('about'), blank=True)
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_('Designates whether this item should be treated as active. '
                    'Unselect this instead of deleting schedule items.')
    )

    class Meta:
        verbose_name = _('schedule item')
        verbose_name_plural = _('schedule items')
        ordering = ('-datetime',)

    def __str__(self):
        return self.title
