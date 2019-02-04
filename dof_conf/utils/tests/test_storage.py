from dof_conf.core.tests import TestCase

from ..storage import upload_to, upload_to_factory


class TestModel(object):

    class _meta:
        app_label = "test"


class StorageTest(TestCase):

    def test_upload_to_factory(self):
        self.assertRegexpMatches(
            upload_to_factory("test")(object(), "test.txt"),
            r"^test/[a-zA-Z0-9\-_]{22}\.txt$"
        )

    def test_upload_to(self):
        self.assertRegexpMatches(
            upload_to(TestModel(), "test.txt"),
            r"^test/testmodel/[a-zA-Z0-9\-_]{22}\.txt$"
        )
