"""
Multithreading in Multiprocessing
"""

import multiprocessing as mp
import threading as td
import time
import logging
import random

logging.basicConfig(level=logging.INFO,
                    format='(%(processName)-9s) %(message)s',)


def doing_something(T=1):
    time.sleep(T)


class MultiThread(td.Thread):
    def __init__(self, queue, *args, **kargs):
        super().__init__(*args, **kargs)
        self.t_queue = queue
        # self.lock = lock
        self.start()
    
    def run(self):
        while True:
            doing_something(T=2)
            # with self.lock:
            value = self.t_queue.get()
            value += 1
            self.t_queue.put(value)
            logging.info(td.current_thread().name + ' : ' + str(value))


def start(queue, n_thread=1):
    logging.info(mp.current_process().name)

    threads = [MultiThread(queue, name=f'MultiThread{i+1}') for i in range(n_thread)]

    for t in threads:
        t.join()

if __name__ == "__main__":
    print(__doc__)

    queue = mp.Queue()
    queue.put(0)

    n_process = 3
    n_thread = 5

    try:
        processes = [mp.Process(target=start, 
                                name=f'MultiProcess{i+1}', 
                                args=(queue, n_thread)) for i in range(n_process)]

        for p in processes:
            p.start()

        for p in processes:
            p.join()
            
    except KeyboardInterrupt:
        for p in processes:
            p.terminate()
