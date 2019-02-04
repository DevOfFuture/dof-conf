from dof_conf.core.tests import TestCase

from . import factories


class TestSpeaker(TestCase):

    def setUp(self):
        self.speaker = factories.SpeakerFactory(name="John Doe")

    def test__str__(self):
        self.assertEqual(self.speaker.__str__(), "John Doe")


class TestScheduleItem(TestCase):

    def setUp(self):
        self.item = factories.ScheduleItem(title="Contributing to Open Source")

    def test__str__(self):
        self.assertEqual(self.item.__str__(), "Contributing to Open Source")
