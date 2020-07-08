# -*- coding: utf-8 -*-

from sqlalchemy.orm import attributes

from tests.unit import base
from app import models

# class AbstractModelTestUpdateFromJson(base.TestCase):
#     @base.TestCase.mock.patch('app.models.AbstractModel.set_values', 'set_values_mock')
#     @base.TestCase.mock.patch('app.models.AbstractModel.save_db')
#     def test_should_call_save_db(self, save_db_mock):
#         instance = self.mock.MagicMock()
#         abstract_model = models.AbstractModel()
#         abstract_model.update_from_json({'oi': 'oi'})
#         self.assertTrue(save_db_mock.called)


class AbstractModelSaveDbTest(base.TestCase):

    @base.TestCase.mock.patch('app.models.db')
    def test_should_call_session_to_commit(self, db_mock):
        session = self.mock.MagicMock()
        db_mock.session = session
        qm = models.AbstractModel()
        qm.save_db()
        self.assertTrue(session.commit.called)

    @base.TestCase.mock.patch('app.models.db')
    def test_should_call_session_to_add(self, db_mock):
        session = self.mock.MagicMock()
        db_mock.session = session
        qm = models.AbstractModel()
        qm.save_db()
        self.assertTrue(session.add.called)

    @base.TestCase.mock.patch('app.models.db')
    def test_should_call_session_to_flush_if_commit_is_false(self, db_mock):
        session = self.mock.MagicMock()
        db_mock.session = session
        qm = models.AbstractModel()
        qm.save_db(commit=False)
        self.assertTrue(session.flush.called)


class SomeTableTest(base.TestCase):

    def test_some_table_must_have_table_name(self):
        self.assertEqual(models.SomeTable.__tablename__, 'some_table')

    def test_some_table_must_have_id_field(self):
        self.assertTrue(isinstance(models.SomeTable.name, attributes.InstrumentedAttribute))

    def test_some_table_must_have_date_of_creation_field(self):
        self.assertTrue(isinstance(models.SomeTable.date_of_creation, attributes.InstrumentedAttribute))
