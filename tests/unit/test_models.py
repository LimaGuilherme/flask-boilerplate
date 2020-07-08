# -*- coding: utf-8 -*-

from sqlalchemy.orm import attributes

from tests.unit import base
from app import models


class SomeTableTest(base.TestCase):

    def test_some_table_must_have_table_name(self):
        self.assertEqual(models.SomeTable.__tablename__, 'some_table')

    def test_some_table_must_have_id_field(self):
        self.assertTrue(isinstance(models.SomeTable.name, attributes.InstrumentedAttribute))

    def test_some_table_must_have_date_of_creation_field(self):
        self.assertTrue(isinstance(models.SomeTable.date_of_creation, attributes.InstrumentedAttribute))
