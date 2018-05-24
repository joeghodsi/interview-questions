'''
Problem: design and implement a call center which has 3 types of employees: respondents, managers,
    directors. A call is answered by the first available respondent. If the respondent can't handle
    the call, they must escalate to a manager. If the manager can't handle it or is not free, they
    must escalate to a director. Implement a method which assigns a call to the first available
    employee

total time: 50min
'''
from queue import Queue


class CallCenter:
    def __init__(self):
        self.active_calls = []
        self.waiting_calls = Queue()
        self.respondents = []
        self.free_respondents = Queue()
        self.managers = []
        self.directors = []

    def dispatch_call(self, call):
        '''dispatches a new call'''
        if len(self.free_respondents) == 0:
            self.waiting_calls.enqueue(call)
            return  # all respondents are currently busy, please wait

        self._dispatch_call(call)

    def escalate(self, call):
        '''escalates a call to the next employee level. can be because the employee is busy or
        not equipped to handle the call'''
        current_employee = call.employee
        next_employee = current_employee.boss

        if not next_employee.free:
            next_employee = next_employee.boss  # simplification: assume director is free

        call.employee = next_employee
        next_employee.free = False
        current_employee.free = True
        if current_employee.role == Role.respondent:
            self.free_respondents.append(current_employee)

    def call_end_receiver(self, call):
        '''listens for signal that call has ended'''
        self.active_calls.remove(call)
        call.employee.free = True

    def employee_free_receiver(self, employee):
        '''listens for signal that employee has become free'''
        self.free_respondents.append(employee)
        next_call = self.waiting_calls.pop()
        if next_call:
            self._dispatch_call(next_call)

    def _dispatch_call(self, call):
        if call.employee:
            return  # the call is already dispatched

        free_respondent = self.free_respondents.pop()
        call.employee = free_respondent
        free_respondent.free = False
        call.start()
        self.active_calls.append(call)


class Call:
    def __init__(self):
        self.waited = 0  # seconds caller has waited
        self.call_length = 0  # seconds call lasted once connected
        self.caller_info = None  # metadata. caller may have entered credit card, phone number, etc
        self.employee = None  # one-to-one employee taking the call

    def start(self):
        pass


class Employee:
    def __init__(self, role):
        self.info = None  # metadata. name, address, phone, etc
        self.role = role or Role.respondent  # role enum: respondent, manager, director
        self.free = True  # whether they are free to take a call
        self.boss = None  # the person this employee reports to


class Role:
    respondent = 0
    manager = 1
    director = 2
