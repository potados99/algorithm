"""This module contains a single function: heap_sort.

You can run a test using this command:
python3 -m doctest cocktail_shaker.py -v
or just
python3 cocktail_shaker.py [--verbose]
"""


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


    return collection


if __name__ == "__main__":
    from common import invoker
    invoker.from_input(heap_sort)
