"""Practice 4

Performance test:
    1. merge sort vs natural merge sort.
    2. tournament sort vs heap sort.
"""


from common import *
from sort import *


def dump_all(x_range):
    dump_sort_function("Merge Sort", merge_sort, x_range)
    dump_sort_function("Natural Merge Sort", , x_range)

    dump_sort_function("Selection Sort", selection_sort, x_range, ylim=60)
    dump_sort_function("Exchange Sort", exchange_sort, x_range, 60)

dump_all(range(1, 200, 5))
