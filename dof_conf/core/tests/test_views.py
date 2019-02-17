from django.shortcuts import reverse

from dof_conf.core.tests import TestCase


class TestHome(TestCase):

    def test_should_render(self):
        url = reverse('core:home')
        response = self.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertInContext('speakers')
        self.assertInContext('schedule')
        self.assertInContext('reservation_form')


class TestReservations(TestCase):

    def setUp(self):
        self.url = reverse('core:reservations')

    def test_render(self):
        response = self.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertInContext('form')
