from abc import ABCMeta, abstractmethod


class Event(metaclass=ABCMeta):

    delta = 0.005

    def __init__(self, time):
        self.time = time

    def __lt__(self, other):
        try:
            return self.time < other.time
        except AttributeError:
            return NotImplemented

    def __gt__(self, other):
        try:
            return self.time > other.time
        except AtttributeError:
            return NotImplemented

    def __eq__(self, other):
        try:
            return abs(self.time - other.time) < Event.delta
        except AttributeError:
            return NotImplemented

    @abstractmethod
    def handle_self(self, Model):
        pass
