"""This module contains a single function: merge_sort.

You can run a test using this command:
python3 -m doctest merge_sort.py -v
or just
python3 merge_sort.py [--verbose]
"""


def merge_sort(collection, verbose=False):
    """Implementation of merge_sort in Python.

    Args:
        collection (list): Input to sort.
        verbose (bool): Print every rotation if true.

    Returns:
        list: The same as the collection, with sort ascending applied.

    Example:
        >>> merge_sort([3, 1, 7, 0, 4, 8, 2])
        [0, 1, 2, 3, 4, 7, 8]

        >>> merge_sort([-91, -123, -1])
        [-123, -91, -1]
    """


    return collection


if __name__ == "__main__":
    from common.invoker import from_input
    from_input(merge_sort)
