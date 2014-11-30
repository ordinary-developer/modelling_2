import unittest
from app.logic.event import Event

class TestEvent(unittest.TestCase):

    def test_create_abstract_class_with_TypeError_exception(self):
        with self.assertRaises(TypeError):
            event = Event(10)
        
