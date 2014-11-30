import math
import random
from queue import PriorityQueue
from app.logic.device import Device
from app.logic.incoming_event import IncomingEvent
from app.logic.outcoming_first_event import OutcomingFirstEvent
from app.logic.outcoming_second_event import OutcomingSecondEvent
from app.logic.request import Request

class Model:

    event_list = None
    work_time = None
    inteval_time = None
    model_time = None


    @staticmethod
    def initialize(work_time_value):
        Model.event_list = PriorityQueue()
        Model.work_time = work_time_value
        Model.interval_time = 60
        Model.model_time = 0.0
        Model.device1 = Device(30, 70)
        Model.device2 = Device(45, 60)
        Model.add_event(IncomingEvent(0.0))

    @staticmethod
    def start():
        while Model.model_time < Model.work_time:
            present_event = Model.get_event()
            Model.model_time = present_event.time
            present_event.handle_self(Model)
                
    @staticmethod
    def add_event(event):
        Model.event_list.put(event)

    @staticmethod
    def get_event():
        return Model.event_list.get()

    @staticmethod
    def get_exp_interval():
        return (-1) * math.log(1 - random.random()) * Model.interval_time

    @staticmethod
    def handle_incoming_event(time):
        event_time = time + Model.get_exp_interval()
        Model.add_event(IncomingEvent(event_time))
        current_request_number = Model.device1.next_request_number
        request = Request(current_request_number, time)
        if Model.device1.present_request != None:
            Model.device1.add_request(request)
        else:
            Model.process_device1(request)
        #log function
        print('[handle an incoming event]\t\t\t{0:.2f} sec.'.format(event_time))

    @staticmethod
    def process_device1(request):
        Model.device1.present_request = request
        Model.device1.next_request_number += 1
        time = Model.device1.get_processing_time()
        totalTime = Model.model_time - request.time
        Model.add_event(OutcomingFirstEvent(Model.model_time + totalTime))
        #log function
        print('<Processing 1-st device>\t\t\trequest {0}'.format(request.number))

    @staticmethod
    def handle_outcoming_first_event(time):
        present_request = Model.device1.present_request
        Model.device1.present_request = None
        if not Model.device1.is_empty_request_queue():
            request = Model.device1.remove_request()
            process_device1(request)
        else:
            Model.device1.preset_request = None
        if Model.device2.present_request != None: 
            Model.device2.add_request(present_request)
        else:
            Model.process_device2(present_request)
        #log function
        print('[handle an outcoming event from 1-st device]\t{0:.2f} sec'.format(
                    time))
                
    @staticmethod
    def process_device2(request):
        Model.device2.present_request = request
        Model.device2.next_request_number += 1
        time = Model.device2.get_processing_time()
        totalTime = Model.model_time - request.time
        Model.add_event(OutcomingSecondEvent(Model.model_time + totalTime))
        #log function
        print('<Processing 2-nd device>\t\t\trequest {0}'.format(request.number))

    @staticmethod
    def handle_outcoming_second_event(time):
        Model.device2.present_request = None
        if not Model.device2.is_empty_request_queue():
            request = Model.device2.remove_request()
            process_device2(request)
        else:
            Model.device2.present_request = None
        #log function
        print('[handling an outcoming event from 2-nd device]\t{0:.2f} sec'.format(
                    time))
                


