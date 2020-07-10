"""
Producer - Customer Problem with 'Condition'
"""

from threading import Thread, Condition
import threading
import queue
import time
import logging

logging.basicConfig(level=logging.INFO,
                    format='(%(threadName)-9s) %(message)s',)


class Producer(Thread):
    def __init__(self, array, condition, *args, **kargs):
        super().__init__(*args, **kargs)
        self.array = array
        self.condition = condition
        self.start()

    def run(self):
        while True:
            time.sleep(1)
            with self.condition:
                logging.info(threading.current_thread().name +
                             ' produces value')
                self.array.append(True)
                self.condition.notify_all()  # self.condition.notify(n=2)


class Consumer(Thread):
    def __init__(self, array, condition, *args, **kargs):
        super().__init__(*args, **kargs)
        self.array = array
        self.condition = condition
        self.start()

    def run(self):
        while True:
            with self.condition:
                # wait until length_of_array > 0
                self.condition.wait_for(lambda: len(self.array) > 0)
                logging.info(threading.current_thread().name +
                             ' consumes value')
                self.array.pop(0)


def main():
    array = []
    condition = Condition()

    p = Producer(array, condition, name='Producer')
    c1 = Consumer(array, condition, name='Consumer1')
    c2 = Consumer(array, condition, name='Consumer2')
    # c3 = Consumer(array, name='Consumer3')

    p.join()
    c1.join()
    c2.join()
    # c3.join()

    print(len(array))


if __name__ == "__main__":
    print(__doc__)
    main()
