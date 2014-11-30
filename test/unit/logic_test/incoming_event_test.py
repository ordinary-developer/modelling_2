import unittest
from app.logic.incoming_event import IncomingEvent

class TestIncomingEvent(unittest.TestCase):

    def setUp(self):
        self.time = 10.0
        self.incoming_event = IncomingEvent(self.time)

    def test_create_incoming_event_with_correct_time(self):
        self.assertAlmostEqual(self.time, self.incoming_event.time)

    def test_create_two_unequal_events(self):
        #[ARRANGE]
        event1 = IncomingEvent(1.0)
        event2 = IncomingEvent(2.0)
        #[ACT - ASSERT]
        self.assertGreater(event2, event1)
        self.assertLess(event1, event2)
        self.assertNotEqual(event1, event2)

    def test_create_two_equal_events(self):
        #[ARRANGE]
        event1 = IncomingEvent(1.0)
        event2 = IncomingEvent(1.0)
        #[ACT - ASSERT]
        self.assertEqual(event1, event2)

