"""Practice 4

Performance test:
    1. merge sort vs natural merge sort.
    2. tournament sort vs heap sort.
"""


from ... import common
from sort import *


def dump_all(x_range):
    dump_sort_function("Merge Sort", merge_sort, x_range)
    dump_sort_function("Natural Merge Sort", natural_merge_sort, x_range)

    dump_sort_function("Tournament Sort", tournament_sort, x_range, ylim=60)
    dump_sort_function("Heap Sort", heap_sort, x_range, 60)

dump_all(range(1, 200, 5))
