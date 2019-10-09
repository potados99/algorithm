"""This module contains a single function: exchange_sort.

You can run a test using this command:
python3 -m doctest cocktail_shaker.py -v
or just
python3 cocktail_shaker.py [--verbose]
"""


def exchange_sort(collection, verbose=False):
    """Implementation of exchange sort in Python.

    Args:
        collection (list): Input to sort.
        verbose (bool): Print every rotation if true.

    Returns:
        list: The same as the collection, with sort ascending applied.

    Example:
        >>> exchange_sort([3, 1, 7, 0, 4, 8, 2])
        [0, 1, 2, 3, 4, 7, 8]

        >>> exchange_sort([-91, -123, -1])
        [-123, -91, -1]
    """

    size = len(collection)

    for i in range(0, size -1):
        for j in range(i, size):
            if collection[i] > collection[j]:
                collection[i], collection[j] = collection[j], collection[i]
                if verbose: print(collection)

    return collection


if __name__ == "__main__":
    from common import invoker
    invoker.from_input(exchange_sort)
