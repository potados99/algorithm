"""This module contains a single function: quick_sort.

You can run a test using this command:
    python3 -m doctest quick_sort.py -v
or just
    python3 quick_sort.py [--verbose]
"""

# This module can be executed as module and script and by doctest.
if __name__ == "__main__" or __name__ == "quick_sort":
    from common.util import *
else:
    from .common.util import *


def partition(collection, left, right):
    """Make left partition le pivot, right partition ge pivot.
    The pivot is selected by picking mid-index.

    Args:
        collection (list): Whole data.
        left (int): Index of start of left partition.
        right (int): Index of end of right partition.

    Returns:
        int: Index of the pivot.

    Example:
        >>> partition([9, 8, 7, 6, 5, 4, 3, 2, 1], 3, 6)
        5
    """

    # Place mid-indexed item at the right end of the collection.
    mid = (left + right) // 2
    swap(collection, mid, right)

    pivot = collection[right]
    i = left - 1

    for j in range(left, right):
        if collection[j] < pivot:
            i += 1
            swap(collection, i, j)

    swap(collection, i + 1, right)

    return i + 1


def quick_sort(collection, verbose=False):
    """Implementation of quick sort in Python.

    Args:
        collection (list): Input to sort.
        verbose (bool): Print every rotation if true.

    Returns:
        list: The same as the collection, with sort ascending applied.

    Example:
        >>> quick_sort([3, 1, 7, 0, 4, 8, 2])
        [0, 1, 2, 3, 4, 7, 8]

        >>> quick_sort([-91, -123, -1])
        [-123, -91, -1]

        >>> quick_sort([])
        []
    """

    stack = list()

    stack.append(0)    # l
    stack.append(len(collection) - 1) # h

    while len(stack) > 0:
        h = stack.pop()
        l = stack.pop()

        # No need for partition for subarray of size 1 or 0.
        if l >= h:
            continue

        if verbose: print("    " * len(stack) + "Partition " + str(collection[l:h+1]), end="")
        p = partition(collection, l, h)
        if verbose: print(", pivot is " + str(collection[p]))

        # Elements on left
        if l < p - 1:
            stack.append(l)
            stack.append(p - 1)

        # Elements on right
        if p + 1 < h:
            stack.append(p + 1)
            stack.append(h)

    return collection


if __name__ == "__main__":
    from common.invoker import from_input
    from_input(quick_sort)
