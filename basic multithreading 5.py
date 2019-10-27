"""
Producer-Consumer problem
"""

import threading
from time import time, sleep
import logging

logging.basicConfig(level=logging.INFO,
                    format='(%(threadName)-9s) %(message)s',)


def producer(condition):
    sleep(0.001)
    logging.info(threading.current_thread().name + ' is running')
    with condition:
        logging.info('producer produced')
        condition.notify_all()


def consumer(condition):
    logging.info(threading.current_thread().name + ' is running')
    with condition:
        condition.wait()
        logging.info('consumer consumed')


def main():
    condition = threading.Condition()

    p = threading.Thread(target=producer, name='Producer', args=(condition,))
    c1 = threading.Thread(target=consumer, name='Consumer1', args=(condition,))
    c2 = threading.Thread(target=consumer, name='Consumer2', args=(condition,))

    # t = [threading.Thread(target=consumer, args=(condition,)) for _ in range(5)]

    start_time = time()

    p.start()
    c1.start()
    c2.start()

    p.join()
    c1.join()
    c2.join()

    print('\nRequried time:', time() - start_time)


if __name__ == '__main__':
    print(__doc__)
    main()
