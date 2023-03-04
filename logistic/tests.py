from rest_framework.test import APIClient
from unittest import TestCase


class ApiTestCase(TestCase):
    def test_testview(self):
        client = APIClient()
        resp = client.get('/api/v1/test/')
        self.assertEqual(resp.status_code, 200)
