"""
Producer - Customer Problem with 'Condition'
"""

from multiprocessing import Process, Lock
import multiprocessing as mp
import queue
import time
import logging
import random

logging.basicConfig(level=logging.INFO,
                    format='(%(processName)-9s) %(message)s',)


class Producer(Process):
    def __init__(self, variable, lock, *args, **kargs):
        super().__init__(*args, **kargs)
        self.variable = variable
        self.lock = lock
        self.start()
    
    def run(self):
        while True:
            time.sleep(1)
            with self.lock:
                value = random.randint(0, 100)
                self.variable.value = value
                logging.info(mp.current_process().name + ' produces value ' + str(value))


class Consumer(Process):
    def __init__(self, variable, lock, *args, **kargs):
        super().__init__(*args, **kargs)
        self.variable = variable
        self.lock = lock
        self.start()
    
    def run(self):
        while True:
            time.sleep(3)
            with self.lock:
                value = self.variable.value
                logging.info(mp.current_process().name + ' consumes value ' + str(value))


def main():
    variable = mp.Value('i', 999)
    lock = Lock()

    p1 = Producer(variable, lock, name='Producer1')
    p2 = Producer(variable, lock, name='Producer2')
    c1 = Consumer(variable, lock, name='Consumer1')
    c2 = Consumer(variable, lock, name='Consumer2')
    c3 = Consumer(variable, lock, name='Consumer3')

    p1.join()
    p2.join()
    c1.join()
    c2.join()
    c3.join()
    
    print(variable)


if __name__ == "__main__":
    print(__doc__)
    main()