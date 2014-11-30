import unittest
from app.logic.request import Request

class RequestTest(unittest.TestCase):

    def setUp(self):
        self.number = 1
        self.time = 10.35
        self.request = Request(self.number, self.time) 

    def test_create_request(self):
        self.assertIsNotNone(self.request)

    def test_create_request_with_number_assertion(self):
        self.assertEqual(self.number, self.request.number)

    def test_create_request_with_time_assertion(self):
        self.assertAlmostEqual(self.time, self.request.time, delta = 0.005)

