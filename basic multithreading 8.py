"""
Producer - Customer Problem with 'Condition'
"""

from threading import Thread, Condition
import threading
import queue
import time
import logging
import random

logging.basicConfig(level=logging.INFO,
                    format='(%(threadName)-9s) %(message)s',)
random.seed(999)


def doing_something():
    time.sleep(1)


class Variable(object):
    def __init__(self, value=None):
        self.value = value

    def set_value(self, value):
        assert value is not None
        self.value = value

    def get_value(self):
        value = self.value
        self.value = None
        return value

    def is_none(self):
        return self.value is None

    def is_not_none(self):
        return self.value is not None

    def __repr__(self):
        return str(self.value)


class Producer(Thread):
    def __init__(self, variable, condition, *args, **kargs):
        super().__init__(*args, **kargs)
        self.variable = variable
        self.condition = condition

    def run(self):
        while True:
            doing_something()
            with self.condition:
                # wait until variable is none
                self.condition.wait_for(self.variable.is_none)
                value = random.randint(0, 100)
                self.variable.set_value(value)
                logging.info(threading.current_thread().name +
                             ' produces value ' + str(value))
                self.condition.notify_all()


class Consumer(Thread):
    def __init__(self, variable, condition, *args, **kargs):
        super().__init__(*args, **kargs)
        self.variable = variable
        self.condition = condition

    def run(self):
        while True:
            doing_something()
            with self.condition:
                # wait until variable is not none
                self.condition.wait_for(self.variable.is_not_none)
                value = self.variable.get_value()
                logging.info(threading.current_thread().name +
                             ' consumes value ' + str(value))
                self.condition.notify_all()


def main():
    variable = Variable()
    condition = Condition()
    processes = []

    processes.append(Producer(variable, condition, name='Producer1'))
    processes.append(Producer(variable, condition, name='Producer2'))
    # processes.append(Producer(variable, condition, name='Producer3'))
    processes.append(Consumer(variable, condition, name='Consumer1'))
    processes.append(Consumer(variable, condition, name='Consumer2'))
    processes.append(Consumer(variable, condition, name='Consumer3'))

    try:
        for p in processes:
            p.start()
        for p in processes:
            p.join()
    except KeyboardInterrupt as e:
        print(e)

    print(variable)


if __name__ == "__main__":
    print(__doc__)
    main()
