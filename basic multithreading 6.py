"""
Empty
"""

from multiprocessing.dummy import Process
import queue
import time
import logging

logging.basicConfig(level=logging.INFO,
                    format='(%(threadName)-9s) %(message)s',)


class Producer(Process):
    def __init__(self, q, *args, **kargs):
        super().__init__(*args, **kargs)
        self.queue = q
        self.start()

    def run(self):
        while True:
            time.sleep(2)
            logging.info('producer produces value')
            self.queue.put(True)


class Consumer(Process):
    def __init__(self, q, *args, **kargs):
        super().__init__(*args, **kargs)
        self.queue = q
        self.start()

    def run(self):
        while True:
            logging.info('consumer consumes value')
            self.queue.get()


def main():
    q = queue.Queue(maxsize=5)

    p = Producer(q, name='Producer')
    c1 = Consumer(q, name='Consumer1')
    c2 = Consumer(q, name='Consumer2')
    # c3 = Consumer(array, name='Consumer3')

    p.join()
    c1.join()
    c2.join()
    # c3.join()


if __name__ == "__main__":
    print(__doc__)
    main()
