from multiprocessing import Process, Value, Lock
from time import time


class Number(object):
    def __init__(self, value=0):
        self.value = Value('i', value)

    def __add__(self, n):
        self.value.value = self.value.value + n

    def __sub__(self, n):
        self.value.value = self.value.value - n

    def __repr__(self):
        return 'Number: {}'.format(self.value.value)


def increment(num, lock=None):
    if lock is not None:
        with lock:
            num = num + 1
    else:
        num = num + 1


def decrement(num, lock=None):
    if lock is not None:
        with lock:
            num = num - 1
    else:
        num = num - 1


def operation_with_race_condition(num, increase=True):
    r = 10 ** 4
    if increase:
        for _ in range(r):
            increment(num)
    else:
        for _ in range(r):
            decrement(num)


def operation_without_race_condition(num, lock, increase=True):
    r = 10 ** 4
    if increase:
        for _ in range(r):
            increment(num, lock)
    else:
        for _ in range(r):
            decrement(num, lock)


def main():
    num = Number(0)
    print('Initial', num)

    start_time = time()

    p1 = Process(target=operation_with_race_condition, name='increment', args=(num, True))
    p2 = Process(target=operation_with_race_condition, name='decrement', args=(num, False))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('After', num)
    print('Time required: {:.6f}'.format(time() - start_time))


    num = Number(0)
    print('\nInitial', num)

    start_time = time()
    lock = Lock()

    p1 = Process(target=operation_without_race_condition, name='increment', args=(num, lock, True))
    p2 = Process(target=operation_without_race_condition, name='decrement', args=(num, lock, False))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('After', num)
    print('Time required: {:.6f}'.format(time() - start_time))


if __name__ == '__main__':
    main()
