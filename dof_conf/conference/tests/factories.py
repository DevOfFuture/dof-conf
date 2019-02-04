from django.utils import timezone
import factory

from dof_conf.core.tests.factories import BaseFactory

from ..models import Speaker, ScheduleItem


class SpeakerFactory(BaseFactory):
    name = factory.Sequence(lambda n: 'Speacker {}'.format(n))

    class Meta:
        model = Speaker
        django_get_or_create = ('name',)


class ScheduleItemFactory(BaseFactory):
    speaker = factory.SubFactory(Speaker)
    title = factory.Sequence(lambda n: 'Schedule item {}'.format(n))
    datetime = factory.LazyFunction(timezone.now)

    class Meta:
        model = ScheduleItem
