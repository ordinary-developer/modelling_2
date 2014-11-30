from collections import deque
import random


class Device:

    def __init__(self, first_value, second_value):
        self.first_value = first_value
        self.second_value = second_value
        self.request_queue = deque()
        self.next_request_number = 0
        self.present_request = None

    def get_processing_time(self):
        r = random.random()
        return self.first_value + (self.second_value - self.first_value) * 4

    def add_request(self, request):
        self.request_queue.append(request)

    def remove_request(self):
        return self.request_queue.popleft()

    def is_empty_request_queue(self):
        return len(self.request_queue) == 0
