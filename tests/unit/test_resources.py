# -*- coding: utf-8 -*-
from tests.unit import base

from app import resources


class CasingTest(base.TestCase):
    def test_should_convert_camel_to_snake(self):
        self.assertEqual(resources.ResourceBase.camel_to_snake('getThisSnaked'), 'get_this_snaked')

    def test_should_convert_snake_to_camel(self):
        self.assertEqual(resources.ResourceBase.snake_to_camel('get_this_camelled'), 'getThisCamelled')

    def test_should_convert_snake_upper_to_camel(self):
        self.assertEqual(resources.ResourceBase.snake_to_camel('GET_THIS_CAMELLED'), 'getThisCamelled')

    def test_should_convert_pascal_to_snake(self):
        self.assertEqual(resources.ResourceBase.camel_to_snake('GetThisSnaked'), 'get_this_snaked')
