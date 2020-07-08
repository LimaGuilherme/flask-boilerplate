# -*- coding: utf-8 -*-

import os
import unittest
from mock import mock
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import database

test_app = Flask(__name__)
test_app.config.from_object('app.config.TestingConfig')

os.environ.update({
    'APP_SETTINGS': 'app.config.TestingConfig',
    'SECRET_KEY': 'SECRET-KEY',
    'DATABASE_URL': 'postgresql+psycopg2://inpro:inpro@localhost/inpro_test',
})

test_app = Flask(__name__)
test_app.config.from_object('app.config.TestingConfig')
test_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database.AppRepository.db = SQLAlchemy(test_app)


class TestCase(unittest.TestCase):
    mock = mock
