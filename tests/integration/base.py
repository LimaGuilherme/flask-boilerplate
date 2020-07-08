# -*- coding: utf-8 -*-
import json
import unittest

import mock
from app import database, initialize


patch = mock.patch


class TestCase(unittest.TestCase):
    mock = mock
    app = initialize.web_app.test_client()
    url = None
    payload = {}

    def setUp(self):
        database.AppRepository.db.create_all()
        self.__cookies = {}
        self.__headers = {'Content-Type': 'application/json', 'Cookie': self.cookies}

    @property
    def cookies(self):
        cookie = ''
        for key, value in self.__cookies.items():
            cookie += '{}={};'.format(key, value)
        return cookie

    def set_cookies(self, cookies):
        self.__cookies = cookies

    @property
    def headers(self):
        return self.__headers

    def set_headers(self, headers):
        self.__headers = headers

    @property
    def get(self):
        return self.app.get(self.url, data=json.dumps(self.payload), headers=self.headers)

    @property
    def post(self):
        return self.app.post(self.url, data=json.dumps(self.payload), headers=self.headers)

    @property
    def post_upload(self):
        return self.app.post(self.url, data=self.payload, headers={'Content-Type': 'multipart/form-data'})

    @property
    def put(self):
        return self.app.put(self.url, data=json.dumps(self.payload), headers=self.headers)

    @property
    def delete(self):
        return self.app.delete(self.url)

    def tearDown(self):
        database.AppRepository.db.session.remove()
        database.AppRepository.db.drop_all()
