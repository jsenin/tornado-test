
from tornado.testing import AsyncHTTPTestCase

import hello

class TestHelloApp(AsyncHTTPTestCase):
    def get_app(self):
        return hello.make_app()

    def test_homepage(self):
        response = self.fetch('/')
        self.assertEqual(response.code, 200)
        self.assertEqual(bytes.decode(response.body), 'Hello, world')
