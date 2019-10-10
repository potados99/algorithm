"""This module contains a single function: natural_merge_sort.

You can run a test using this command:
python3 -m doctest natural_merge_sort.py -v
or just
python3 natural_merge_sort.py [--verbose]
"""


def natural_merge_sort(collection, verbose=False):
    """Implementation of natural merge sort in Python.

    Args:
        collection (list): Input to sort.
        verbose (bool): Print every rotation if true.

    Returns:
        list: The same as the collection, with sort ascending applied.

    Example:
        >>> natural_merge_sort([3, 1, 7, 0, 4, 8, 2])
        [0, 1, 2, 3, 4, 7, 8]

        >>> natural_merge_sort([-91, -123, -1])
        [-123, -91, -1]
    """


    return collection


if __name__ == "__main__":
    from common.invoker import from_input
    from_input(natural_merge_sort)
