# -*- coding: utf-8 -*-

from tests.integration import base


class GETSomethingTest(base.TestCase):

    url = '/api/something'

    def test_get_something_should_return_ok(self):
        response = self.get
        self.assertEqual(response.status_code, 200)

    def test_get_specific_something_should_return_ok(self):
        self.url = 'api/something/{}'.format(1)
        response = self.get
        self.assertEqual(response.status_code, 200)


class POSTSomethingTest(base.TestCase):

    url = '/api/something'

    def test_post_something_should_return_method_not_allowed(self):
        response = self.post
        self.assertEqual(response.status_code, 405)


class PUTSomethingTest(base.TestCase):

    url = '/api/something'

    def test_put_something_should_return_method_not_allowed(self):
        response = self.put
        self.assertEqual(response.status_code, 405)


class DELETESomethingTest(base.TestCase):

    url = '/api/something'

    def test_delete_something_should_return_method_not_allowed(self):
        response = self.put
        self.assertEqual(response.status_code, 405)
