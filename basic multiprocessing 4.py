import multiprocessing as mps
from multiprocessing.pool import Pool, ThreadPool
from multiprocessing.dummy import Process
from time import time


def add_one(x):
    return x + 1


def single_process(my_list):
    start_time = time()

    result = list(map(add_one, my_list))

    print(single_process.__name__,
          '\nRequired time: {:.6f}\n'.format(time() - start_time),
          result[-5:], end='\n\n')


def sync_multiprocess(my_list):
    pool = Pool()

    start_time = time()

    result = pool.map(add_one, my_list)
    pool.close()

    print(sync_multiprocess.__name__,
          '\nRequired time: {:.6f}\n'.format(time() - start_time),
          result[-5:], end='\n\n')


def async_multiprocess(my_list):
    pool = Pool()

    start_time = time()

    result = pool.map_async(add_one, my_list)
    pool.close()

    print(async_multiprocess.__name__,
          '\nRequired time: {:.6f}\n'.format(time() - start_time),
          result.get()[-5:], end='\n\n')


def sync_multi_thread(my_list):
    pool = ThreadPool()

    start_time = time()

    result = pool.map(add_one, my_list)
    pool.close()

    print(sync_multi_thread.__name__,
          '\nRequired time: {:.6f}\n'.format(time() - start_time),
          result[-5:], end='\n\n')


def async_multi_thread(my_list):
    pool = ThreadPool()

    start_time = time()

    result = pool.map_async(add_one, my_list)
    pool.close()

    print(async_multi_thread.__name__,
          '\nRequired time: {:.6f}\n'.format(time() - start_time),
          result.get()[-5:], end='\n\n')


def main():
    my_list = list(range(10 ** 6))

    single_process(my_list)

    sync_multiprocess(my_list)
    async_multiprocess(my_list)

    sync_multi_thread(my_list)
    async_multi_thread(my_list)


if __name__ == '__main__':
    main()
