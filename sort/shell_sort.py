"""This module contains three functions:
shell_sort, subarray_insertion_sort, and round_odd.

You can run a test using this command:
python3 -m doctest shell_sort.py -v
or just
python3 shell_sort.py [--verbose]
"""


def round_odd(number):
    """Round number to odd by adding 1 if it is even.

    Args:
        number (int): The number we want to round.

    Returns:
        int: Rounded number.

    Example:
        >>> round_odd(3)
        3

        >>> round_odd(4)
        5
    """
    return number + 1 if number % 2 == 0 else number


def subarray_insertion_sort(collection, first, last, gap, verbose=False):
    """Insertion sort among elements with gap.

    Args:
        collection (list): Input to sort.
        first (int): Index of first element to apply sort.
        last (int): Index of last element to apply sort.
        gap (int): Interval between elements to sort.
        verbose (bool): Print every rotation if true.

    Returns:
        list: The same as the collection, with sort ascending applied.

    Example:
        >>> subarray_insertion_sort([7, 345, 6, 5, 128, 4, 3, 243], 1, 7, 3)
        [7, 128, 6, 5, 243, 4, 3, 345]
    """

    if verbose:
        print("first: " + str(first) + " last: " + str(last) + " gap:  " + str(gap))
        print(collection)

    rotation = 1

    for i in range(first + gap, last + 1, gap):
        if verbose: print("        Rotation " + str(rotation))

        n = collection[i]

        # j from i - 1 to 0.
        for j in range(i - gap, first - gap - 1, -gap):
            if collection[j] <= n: break

            collection[j + gap] = collection[j]
            if verbose: print(collection)

        collection[j + gap] = n

        if verbose: print(collection)

        rotation += 1

    return collection


def shell_sort(collection, verbose=False):
    """Implementation of shell sort in Python.

    Args:
        collection (list): Input to sort.
        verbose (bool): Print every rotation if true.

    Returns:
        list: The same as the collection, with sort ascending applied.

    Example:
        >>> shell_sort([3, 1, 7, 0, 4, 8, 2])
        [0, 1, 2, 3, 4, 7, 8]

        >>> shell_sort([-91, -123, -1])
        [-123, -91, -1]

        >>> shell_sort([])
        []
    """

    size = len(collection)
    gap = round_odd(size >> 1)
    rotation = 1

    while gap > 0:
        if verbose: print("Rotation " + str(rotation))

        gap = round_odd(gap)

        # Number of subarrays: gap
        for i in range(0, gap + 1):
            subarray_insertion_sort(collection, i, size - 1, gap, verbose)

        gap = gap >> 1
        rotation += 1

    return collection


if __name__ == "__main__":
    from common.invoker import from_input
    from_input(shell_sort)
