import time
import copy
import random


def elapsed_time(body):
    time_bgn = time.time()
    body()
    elapsed_millis = (time.time() - time_bgn) * 1000.0
    return elapsed_millis


def average(collection):
    """
    Example:
        >>> average([3, 4, 5])
        4.0
    """
    return sum(collection) / len(collection)


def random_list(size):
    return [random.randint(1, 512) for i in range(size)]


def ordered_list(size):
    """
    Example:
        >>> ordered_list(4)
        [1, 2, 3, 4]
    """
    return list(range(1, size + 1))


def reverse_ordered_list(size):
    """
    Example:
        >>> reverse_ordered_list(4)
        [4, 3, 2, 1]
    """
    return list(range(size, 0, -1))


def copy_list(origin):
    return copy.deepcopy(origin)


def swap(list, a, b):
    list[a], list[b] = list[b], list[a]
