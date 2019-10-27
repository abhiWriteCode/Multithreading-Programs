import multiprocessing as mps
import os


def A(x):
    print("\nID of parent process of this program: {}".format(os.getppid()))
    print("ID of process running A program: {}".format(os.getpid()))
    for i in range(1, x+1):
        print('A', i**2)


def B(x):
    print("\nID of parent process of this program: {}".format(os.getppid()))
    print("ID of process running B program: {}".format(os.getpid()))
    for i in range(1, x+1):
        print('B', i**3)


if __name__ == '__main__':
    print("\nID of process running main program: {}".format(os.getpid()))

    p1 = mps.Process(target=A, name='square', args=(50,))
    p2 = mps.Process(target=B, name='cube', args=(50,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
