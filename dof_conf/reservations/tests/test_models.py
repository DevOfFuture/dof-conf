from dof_conf.core.tests import TestCase

from . import factories


class TestReservation(TestCase):

    def setUp(self):
        self.reservation = factories.Reservation(name='John Doe')

    def test__str__(self):
        self.assertEqual(self.reservation.__str__(), 'John Doe')
