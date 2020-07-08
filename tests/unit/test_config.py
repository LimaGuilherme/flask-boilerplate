# -*- coding: utf-8 -*-
from tests.unit import base
from app import resources, config as config_module

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

    def test_has_AMBIENTE(self):
        self.assertTrue(hasattr(self.config, 'AMBIENTE'))


class StagingConfigTest(base.TestCase):

    def setUp(self):
        super(StagingConfigTest, self).setUp()
        self.config = config

    def test_has_AMBIENTE(self):
        self.assertTrue(hasattr(self.config, 'AMBIENTE'))

    def test_has_DEBUG(self):
        self.assertTrue(hasattr(self.config, 'DEBUG'))

    def test_has_DEBUG_default_true(self):
        self.assertTrue(self.config.DEBUG)


class DevelopmentConfigTest(base.TestCase):

    def setUp(self):
        super(DevelopmentConfigTest, self).setUp()
        self.config = config

    def test_has_AMBIENTE(self):
        self.assertTrue(hasattr(self.config, 'AMBIENTE'))

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

    def test_has_AMBIENTE(self):
        self.assertTrue(hasattr(self.config, 'AMBIENTE'))

    def test_has_DEBUG(self):
        self.assertTrue(hasattr(self.config, 'DEBUG'))

    def test_has_SQLALCHEMY_RECORD_QUERIES(self):
        self.assertTrue(hasattr(self.config, 'SQLALCHEMY_RECORD_QUERIES'))

    def test_has_DEBUG_default_true(self):
        self.assertTrue(self.config.DEBUG)

    def test_has_SQLALCHEMY_RECORD_QUERIES_default_true(self):
        self.assertTrue(self.config.SQLALCHEMY_RECORD_QUERIES)
