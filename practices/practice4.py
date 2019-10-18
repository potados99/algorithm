"""Practice 4

Performance test:
    1. merge sort vs natural merge sort.
    2. tournament sort vs heap sort.

Run it using following command:
    python3 practice4.py
"""


import sys;
import os.path as o
sys.path.append(o.abspath(o.join(o.dirname(sys.modules[__name__].__file__), "..")))

from sort.common.dump import *
from sort.merge_sort import *
from sort.natural_merge_sort import *
from sort.tournament_sort import *
from sort.heap_sort import *

def dump_all(x_range):
    dump_sort_function("Merge Sort", merge_sort, x_range, y_limit=100)
    dump_sort_function("Natural Merge Sort", natural_merge_sort, x_range, y_limit=100)

    dump_sort_function("Tournament Sort", tournament_sort, x_range, y_limit=60)
    dump_sort_function("Heap Sort", heap_sort, x_range, y_limit = 60)

dump_all(range(1, 1000, 5))
