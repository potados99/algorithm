import time
import copy
import random

def elapsed_time(body):
    time_bgn = time.time()
    body()
    elapsed_millis = (time.time() - time_bgn) * 1000.0
    return elapsed_millis

def average(collection):
    return sum(collection) / len(collection)

def random_list(size):
    return [random.randint(1, 512) for i in range(size)]

def ordered_list(size):
    return list(range(1, size))

def reverse_ordered_list(size):
    return list(range(size, 0, -1))

def copy_list(origin):
    return copy.deepcopy(origin)
