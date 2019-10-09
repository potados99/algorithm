"""This module contains a single function: bubble_sort.

You can run a test using this command:
python3 -m doctest bubble_sort.py -v
or just
python3 bubble_sort.py [--verbose]
"""


def bubble_sort(collection, verbose=False):
    """Implementation of bubble sort in Python.

    Args:
        collection (list): Input to sort.
        verbose (bool): Print every rotation if true.

    Returns:
        list: The same as the collection, with sort ascending applied.

    Example:
        >>> bubble_sort([3, 1, 7, 0, 4, 8, 2])
        [0, 1, 2, 3, 4, 7, 8]

        >>> bubble_sort([-91, -123, -1])
        [-123, -91, -1]
    """

    for i in range(0, len(collection) - 1):
        if verbose: print("Rotation " + str(i + 1))

        for j in range(0, len(collection) - 1):
            if (collection[j] > collection[j + 1]):
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
                if verbose: print(collection)

    return collection


if __name__ == "__main__":
    from common import invoker
    invoker.from_input(bubble_sort)
