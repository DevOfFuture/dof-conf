from django.shortcuts import reverse

from dof_conf.core.tests import TestCase


class TestHome(TestCase):

    def test_should_render(self):
        url = reverse('core:home')
        response = self.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertInContext('speakers')
        self.assertInContext('schedule')
