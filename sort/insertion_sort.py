"""This module contains a single function: insertion_sort.

You can run a test using this command:
python3 -m doctest cocktail_shaker.py -v
or just
python3 cocktail_shaker.py [--verbose]
"""


def insertion_sort(collection, verbose=False):
    """Implementation of insertion sort in Python.

    Args:
        collection (list): Input to sort.
        verbose (bool): Print every rotation if true.

    Returns:
        list: The same as the collection, with sort ascending applied.

    Example:
        >>> insertion_sort([3, 1, 7, 0, 4, 8, 2])
        [0, 1, 2, 3, 4, 7, 8]

        >>> insertion_sort([-91, -123, -1])
        [-123, -91, -1]
    """

    for i in range(1, len(collection)):
        if verbose: print("Rotation " + str(i))

        n = collection[i]

        # j from i - 1 to 0.
        for j in range(i - 1, -2, -1):
            if collection[j] <= n: break

            collection[j + 1] = collection[j]
            if verbose: print(collection)

        collection[j + 1] = n

        if verbose: print(collection)

    return collection


if __name__ == "__main__":
    from common import invoker
    invoker.from_input(insertion_sort)
