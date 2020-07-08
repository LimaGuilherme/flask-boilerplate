# -*- coding: utf-8 -*-
from tests.unit import base
from app import config as config_module, exceptions

config = config_module.get_config()


class ConfigTest(base.TestCase):

    def setUp(self):
        super(ConfigTest, self).setUp()
        self.config = config

    def test_has_DEBUG(self):
        self.assertTrue(hasattr(self.config, 'DEBUG'))

    def test_has_REDIS_URL(self):
        self.assertTrue(hasattr(self.config, 'REDIS_URL'))


class ProductionConfigTest(base.TestCase):

    def setUp(self):
        super(ProductionConfigTest, self).setUp()
        self.config = config

    def test_has_ENVIRONMENT(self):
        self.assertTrue(hasattr(self.config, 'ENVIRONMENT'))


class StagingConfigTest(base.TestCase):

    def setUp(self):
        super(StagingConfigTest, self).setUp()
        self.config = config

    def test_has_ENVIRONMENT(self):
        self.assertTrue(hasattr(self.config, 'ENVIRONMENT'))

    def test_has_DEBUG(self):
        self.assertTrue(hasattr(self.config, 'DEBUG'))

    def test_has_DEBUG_default_true(self):
        self.assertTrue(self.config.DEBUG)


class DevelopmentConfigTest(base.TestCase):

    def setUp(self):
        super(DevelopmentConfigTest, self).setUp()
        self.config = config

    def test_has_ENVIRONMENT(self):
        self.assertTrue(hasattr(self.config, 'ENVIRONMENT'))

    def test_has_DEVELOPMENT(self):
        self.assertTrue(hasattr(self.config, 'DEVELOPMENT'))

    def test_has_DEBUG(self):
        self.assertTrue(hasattr(self.config, 'DEBUG'))

    def test_has_SQLALCHEMY_RECORD_QUERIES(self):
        self.assertTrue(hasattr(self.config, 'SQLALCHEMY_RECORD_QUERIES'))

    def test_has_DEBUG_default_true(self):
        self.assertTrue(self.config.DEBUG)

    def test_has_DEVELOPMENT_default_true(self):
        self.assertTrue(self.config.DEVELOPMENT)

    def test_has_SQLALCHEMY_RECORD_QUERIES_default_true(self):
        self.assertTrue(self.config.SQLALCHEMY_RECORD_QUERIES)


class SandboxConfigTest(base.TestCase):

    def setUp(self):
        super(SandboxConfigTest, self).setUp()
        self.config = config

    def test_has_ENVIRONMENT(self):
        self.assertTrue(hasattr(self.config, 'ENVIRONMENT'))

    def test_has_DEBUG(self):
        self.assertTrue(hasattr(self.config, 'DEBUG'))

    def test_has_SQLALCHEMY_RECORD_QUERIES(self):
        self.assertTrue(hasattr(self.config, 'SQLALCHEMY_RECORD_QUERIES'))

    def test_has_DEBUG_default_true(self):
        self.assertTrue(self.config.DEBUG)

    def test_has_SQLALCHEMY_RECORD_QUERIES_default_true(self):
        self.assertTrue(self.config.SQLALCHEMY_RECORD_QUERIES)


class GetConfigTest(base.TestCase):

    @base.mock.patch('app.config.import_module')
    def test_should_call_import_module_to_import_config_module(self, import_module_mock):
        config_module.get_config()
        self.assertTrue(import_module_mock.called)
