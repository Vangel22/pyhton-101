# Multithreading is a way of achieving multitasking

# Process in Python has 3 basic components
# 1. An executable program
# 2. The assosiated data needed by the program (variables, workspace, buffers, etc...)
# 3. The execution context of the program (State of the process)

# A thread contains all the thread information in a thread control block or TCB
# TCB contains:
# 1. Thread Identifier: Unique id (TID) is assigned to every new thread
# 2. Stack pointer: Points to the thread’s stack in the process.
#    The stack contains the local variables under the thread’s scope.
# 3. Program counter: a register that stores the address of the instruction currently
#    being executed by a thread.
# 4. Thread state: can be running, ready, waiting, starting, or done.
# 5. Thread’s register set: registers assigned to thread for computations.
# 6. Parent process Pointer: A pointer to the Process control block (PCB) of the process
#    that the thread lives on.


# Multiple threads can exist within one process where:
# 1. Each thread has its own register set and local variables (stored in the stack)
# 2. All threads of a process share global variables (stored in heap - binary three) and the program code

# Context switching is a process in which the state of the current state is saved and the state of the
# next thread is being loaded on a I/O interruption.

import threading
import os

# t1 = threading.Thread(target, args)
# t2 = threading.Thread(target, args)

# t1.start()
# t2.start()

#  In order to stop the execution of the current program until a thread is complete,
# we use the join() method.
# t1.join()
# t2.join()


def print_cube(num):
    # function to print cube of given num
    print("Cube: {}" .format(num * num * num))


def print_square(num):
    # function to print square of given num
    print("Square: {}" .format(num * num))


def task1():
    print("Task 1 assigned to thread: {}".format(
        threading.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid()))


def task2():
    print("Task 2 assigned to thread: {}".format(
        threading.current_thread().name))
    print("ID of process running task 2: {}".format(os.getpid()))


if __name__ == "__main__":
    # t1 = threading.Thread(target=print_cube, args=(10,))
    # t2 = threading.Thread(target=print_square, args=(10,))

    # print ID of current process
    print("ID of process running main program: {}".format(os.getpid()))

    # print name of main thread
    print("Main thread name: {}".format(threading.current_thread().name))

    # creating threads
    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')

    t1.start()
    t2.start()

    # .join - wait until thread is terminated
    t1.join()
    t2.join()

    print('Done!')
