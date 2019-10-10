"""This module contains a single function: selection_sort.

You can run a test using this command:
python3 -m doctest cocktail_shaker.py -v
or just
python3 cocktail_shaker.py [--verbose]
"""


def selection_sort(collection, verbose=False):
    """Implementation of selection_sort in Python.

    Args:
        collection (list): Input to sort.
        verbose (bool): Print every rotation if true.

    Returns:
        list: The same as the collection, with sort ascending applied.

    Example:
        >>> selection_sort([3, 1, 7, 0, 4, 8, 2])
        [0, 1, 2, 3, 4, 7, 8]

        >>> selection_sort([-91, -123, -1])
        [-123, -91, -1]
    """

    for i in range(0, len(collection) - 1):
        if verbose: print("Rotation " + str(i + 1))

        min_index = i

        # Find the index of the minimum item.
        for j in range(i, len(collection)):
            if collection[j] < collection[min_index]: min_index = j

        # Swap if found something smaller than it has.
        if min_index != i:
            collection[min_index], collection[i] = collection[i], collection[min_index]
            if verbose: print(collection)

    return collection


if __name__ == "__main__":
    from invoker import from_input
    from_input(selection_sort)
