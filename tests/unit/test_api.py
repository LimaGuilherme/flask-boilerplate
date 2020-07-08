# -*- coding: utf-8 -*-

from tests.unit import base

from app import api


class ApiTest(base.TestCase):

    @base.TestCase.mock.patch('app.resources.SomeResource', 'SomeResource')
    @base.TestCase.mock.patch('app.api.Api')
    def test_should_check_with_some_resource_end_point_exists(self, api_mock):
        api_instance = self.mock.MagicMock()
        api_mock.return_value = api_instance
        api.create_api('APP')
        api_instance.add_resource.assert_any_call('SomeResource',
                                                  '/api/something',
                                                  '/api/something/<int:something_id>')
