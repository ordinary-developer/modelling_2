import unittest
from app.logic.device import Device
from app.logic.request import Request


class TestDevice(unittest.TestCase):

    def setUp(self):
        self.first_value = 35
        self.second_value = 70
        self.device = Device(self.first_value, self.second_value)

    def test_create_device_with_correct_interval1(self):
        self.assertEqual(self.first_value, self.device.first_value)

    def test_create_device_with_correct_interval2(self):
        self.assertEqual(self.second_value, self.device.second_value)

    def test_create_device_with_correct_request_queue(self):
        self.assertIsNotNone(self.device.request_queue)

    def test_return_non_zero_processing_time_for_device(self):
        self.assertGreater(self.device.get_processing_time(), 0)
        self.assertGreaterEqual(self.device.get_processing_time(),
                self.device.first_value)

    def test_add_request_method(self):
        device = Device(self.first_value, self.second_value)
        device.add_request(Request(1, 20))
        self.assertIsNotNone(device.request_queue)
        self.assertEqual(1, len(device.request_queue))

    def test_remove_request_method(self):
        device = Device(self.first_value, self.second_value)
        device.add_request(Request(1, 20))
        device.add_request(Request(2, 40))

        request = device.remove_request()

        self.assertEqual(1, len(device.request_queue))
        self.assertEqual(1, request.number)
        
    def test_is_empty_request_queue_method1(self):
        #[ASSERT]
        self.assertTrue(self.device.is_empty_request_queue())

    def test_is_empty_request_queue_method2(self):
        #[ARRANGE]
        device = Device(self.first_value, self.second_value)
        device.add_request(Request(1, 20))
        #[ASSERT] 
        self.assertFalse(device.is_empty_request_queue())
