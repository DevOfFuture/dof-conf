import factory

from dof_conf.core.tests.factories import BaseFactory

from ..models import Reservation


class ReservationFactory(BaseFactory):
    name = factory.Sequence(lambda n: 'Reservation {}'.format(n))
    email = factory.Sequence(lambda n: 'reservation{}@example.com'.format(n))

    class Meta:
        model = Reservation
        django_get_or_create = ('email',)
