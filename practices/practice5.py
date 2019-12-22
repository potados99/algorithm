"""Practice 4

Performance test:
    1. Binary search tree vs red-black tree vs AVL tree.

Run it using following command:
    python3 practice5.py
"""

import sys;
import os.path as o
sys.path.append(o.abspath(o.join(o.dirname(sys.modules[__name__].__file__), "..")))

from search.bst import *
from search.rbtree import *
from search.common.dump import *

def dump_all(x_range):
    #dump_search_function("Binary Search Tree Insertion and Search", lambda: BST(), lambda key: key, x_range, y_limit=70)
    #dump_search_function("Red Black Tree Insertion and Search", lambda: RBTree(), lambda key: key, x_range, y_limit=70)
    dump_search_function("PATRICIA Tree Insertion and Search", lambda: RBTree(), lambda key: key, x_range, y_limit=70)

dump_all(range(1, 1000, 5))
