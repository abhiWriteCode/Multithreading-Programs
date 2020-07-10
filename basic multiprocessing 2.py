"""
Value sharing between two processes
"""

import multiprocessing as mps
import os


def process_log(x):
    print(f'Current process ID: {os.getpid()}'
          f'\nName:             {mps.current_process().name}'
          f'\nValue:            {x[:]}\n')


def process_task(x, lock):
    for i, _ in enumerate(x):
        with lock:
            x[i] = x[i] ** 2
    process_log(x)


def main():
    my_list = [1, 2, 3, 4]
    # x = mps.Value('i', 0) and to get value use, x.value
    x = mps.Array('i', my_list)

    lock = mps.Lock()

    process_log(x)

    # creating threads
    p1 = mps.Process(target=process_task, name='Process 1', args=(x, lock))
    p2 = mps.Process(target=process_task, name='Process 2', args=(x, lock))

    # start threads
    p1.start()
    p2.start()

    # wait until threads finish their job
    p1.join()
    p2.join()

    process_log(x)


if __name__ == '__main__':
    print(__doc__)
    main()
