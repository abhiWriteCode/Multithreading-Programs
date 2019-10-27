"""
Exchanging objects between processes
Producer-Consumer problem
"""

from multiprocessing import Queue, Process, Array
from time import time


def is_sorted(l):
    return all(l[i] <= l[i + 1] for i in range(len(l) - 1))


def producer(queue):
    for i in range(10000):
        queue.put(i)


def consumer(queue, arr):
    for i in range(10000):
        arr[i] = queue.get()


def main():
    queue = Queue(maxsize=5)
    arr = Array('i', range(10000))

    p1 = Process(target=producer, name='Producer', args=(queue,))
    p2 = Process(target=consumer, name='Consumer', args=(queue, arr))

    start_time = time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Requried time:', time() - start_time)

    arr = list(arr[:])
    print('Was syncronized ? :', is_sorted(arr))


if __name__ == '__main__':
    print(__doc__)
    main()
