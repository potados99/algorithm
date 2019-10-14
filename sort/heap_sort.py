"""This module contains heap_sort and its helper functions.

You can run a test using this command:
    python3 -m doctest heap_sort.py -v
or just
    python3 heap_sort.py [--verbose]
"""


from common.util import *


def left_child(node):
    return (2 * node) + 1


def right_child(node):
    return (2 * node) + 2


def parent(node):
    return (node - 1) >> 1


def is_leaf(collection, node):
    """Check if this node has no children.

    Args:
        collection (list): Whole tree
        node (int): Index of node in array(or list) representation.

    Returns:
        bool: True if it has no children.

    Example:
        >>> is_leaf([3, 2, 4, 5, 1, 7], 0)
        False
        >>> is_leaf([3, 2, 4, 5, 1, 7], 2)
        False
        >>> is_leaf([3, 2, 4, 5, 1, 7], 3)
        True
    """
    return len(collection) < left_child(node) + 1


def max_heapify(collection, root, heap_size):
    """Make it a max heap.
    Assume that subtrees are max heap.

    Args:
        collection (list): Partially heapified tree.
        root (int): Index of node to use as root node.
        heap_size (int): Size of heap to apply heapify.

    Returns:
        list: The heapified collection.

    Example:
        >>> max_heapify([3, 2, 5, 6, 8], 0, 3)
        [5, 2, 3, 6, 8]
        >>> max_heapify([3, 2, 5, 6, 8], 1, 5)
        [3, 8, 5, 6, 2]
        >>> max_heapify([3, 5, 8, 4, 2, 1, 6], 0, 7)
        [8, 5, 6, 4, 2, 1, 3]
        >>> max_heapify([2, 4, 7, 0, 1, 3, 8], 0, 6)
        [7, 4, 3, 0, 1, 2, 8]
    """

    left = left_child(root)
    right = right_child(root)

    bigger_one = root

    if left < heap_size and collection[left] > collection[bigger_one]:
        bigger_one = left

    if right < heap_size and collection[right] > collection[bigger_one]:
        bigger_one = right

    if bigger_one == root:
        return collection
    else:
        swap(collection, bigger_one, root)
        return max_heapify(collection, bigger_one, heap_size)


def heap_sort(collection, verbose=False):
    """Implementation of heap sort in Python.

    Args:
        collection (list): Input to sort.
        verbose (bool): Print every rotation if true.

    Returns:
        list: The same as the collection, with sort ascending applied.

    Example:
        >>> heap_sort([3, 1, 7, 0, 4, 8, 2])
        [0, 1, 2, 3, 4, 7, 8]

        >>> heap_sort([-91, -123, -1])
        [-123, -91, -1]
    """

    size = len(collection)
    last_subtree_root = (size << 1) - 1

    # 1. Build max heap.
    if verbose: print("Build max heap.")
    for i in range(last_subtree_root, -1, -1):
        max_heapify(collection, i, size)
        if verbose: print(collection)

    # 2. Send root to the end of the list.
    if verbose: print("Pick from root.")
    for i in range(size - 1, 0, -1):
        swap(collection, 0, i)
        if verbose: print(collection)
        max_heapify(collection, 0, i)
        if verbose: print(collection)

    return collection


if __name__ == "__main__":
    from common.invoker import from_input
    from_input(heap_sort)
