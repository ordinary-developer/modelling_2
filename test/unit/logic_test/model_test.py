import unittest
from app.logic.model import Model


class TestModel(unittest.TestCase):

    def setUp(self):
        self.work_time = 60 * 60 * 8
        Model.initialize(self.work_time)

    def test_initialize_model_with_correct_work_time(self):
        self.assertAlmostEqual(self.work_time, Model.work_time, delta = 0.005) 

    def test_create_event_list_not_none(self):
        self.assertIsNotNone(Model.event_list)

    def test_initialize_model_with_correct_model_time(self):
        self.assertAlmostEqual(0, Model.model_time, delta = 0.005)

    def test_initialize_model_with_correct_interval_time(self):
        self.assertEqual(60, Model.interval_time)

    def test_initialize_model_with_not_none_devices(self):
        self.assertIsNotNone(Model.device1)
        self.assertIsNotNone(Model.device2)

    def test_initialize_model_with_start_event_adding(self):
        self.assertEqual(1, Model.event_list.qsize())

    def test_initialize_model_with_not_zero_exp_interval(self):
        self.assertGreater(Model.get_exp_interval(),0)

    def test_handle_incoming_event(self):
        #[ARRANGE]
        time = 10.5
        #[ACT]
        Model.handle_incoming_event(time)
        #[ASSERT]
        self.assertGreater(Model.event_list.qsize(), 0)

