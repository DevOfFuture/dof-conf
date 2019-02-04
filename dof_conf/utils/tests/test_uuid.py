from dof_conf.core.tests import TestCase

from ..uuid import uuid


class UuidTest(TestCase):

    # It's hard to test random data, but more iterations makes the tests
    # more robust.
    TEST_ITERATIONS = 1000

    def testUuidFormat(self):
        for _ in range(self.TEST_ITERATIONS):
            self.assertRegexpMatches(uuid(), r"^[a-zA-Z0-9\-_]{22}$")

    def testUuidUnique(self):
        generated_uuids = set()
        for _ in range(self.TEST_ITERATIONS):
            new_uuid = uuid()
            self.assertNotIn(new_uuid, generated_uuids)
            generated_uuids.add(new_uuid)
