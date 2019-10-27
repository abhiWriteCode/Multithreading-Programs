import threading
import os


def A(x):
    for i in range(x):
        print('A', i)


def B(x):
    for i in range(x):
        print('B', i)


if __name__ == '__main__':
    t1 = threading.Thread(target=A, name='square', args=(30,))
    t2 = threading.Thread(target=B, name='cube', args=(30,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
