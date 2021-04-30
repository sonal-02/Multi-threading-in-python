# find the addition of square and cude of a number using multithreading.


def square(n):
    
    return n ** 2

def cube(n):

    return n ** 3



import threading
from queue import Queue


def addition_of_sq_cube(n):
  
    threads_list = []
    result_list = []

    que = Queue()

    t1 = threading.Thread(target=lambda q, arg1: q.put(square(arg1)), args=(que, n), name="t1")
    t2 = threading.Thread(target=lambda q, arg1: q.put(cube(arg1)), args=(que, n), name="t1")
   

    t1.start()
    t2.start()

    threads_list.extend([t1, t2])
    for t in threads_list:
        t.join()

    while not que.empty():
        get_result = que.get()
       	result_list.append(get_result)

    result = sum(result_list)
    return result
