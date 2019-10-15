"""This module contains a single function: natural_merge_sort.

You can run a test using this command:
python3 -m doctest natural_merge_sort.py -v
or just
python3 natural_merge_sort.py [--verbose]
"""

from merge_sort import merge


def find_two_runs(collection, prev_run_end, until, verbose=False, level=0):
    """Find first two sorted subarray from collection.

    Example:
        >>> find_two_runs([3, 2, 5, 9, 7, 8], 0, 5, False, 0)
        (0, 0, 3)
        >>> find_two_runs([3, 2, 5, 9, 7, 8], 1, 5, False, 0)
        (1, 3, 5)
        >>> find_two_runs([1, 2, 3, 4], 0, 3, False, 0)
        (0, -1, 3)
    """

    i = prev_run_end
    run_starts = []
    last_item = collection[i]

    while i <= until:
        if collection[i] < last_item:
            run_starts.append(i)
            if len(run_starts) >= 2:
                return (0, run_starts[0] - 1, run_starts[1] - 1)

        last_item = collection[i]
        i += 1

    if len(run_starts) >= 1:
        # The second run finishes with the end of collection.
        return (0, run_starts[0] - 1, until)
    else:
        # All sorted.
        return (0, -1, until)


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

    # natural_merge_sort_recursive(collection, 0, len(collection) - 1, verbose, 0)

    if verbose: print("1. Find two runs:")
    l, m, r = find_two_runs(collection, 0, len(collection) - 1, verbose, 0)
    if verbose: print(str(collection[l:m+1]) + " and " + str(collection[m+1:r+1]))

    while m != -1:
        if verbose: print("2. Merge them:")
        merge(collection, l, m, r, verbose, 0)
        if verbose: print("")

        if verbose: print("1. Find two runs:")
        l, m, r = find_two_runs(collection, r, len(collection) - 1, verbose, 0)
        if verbose: print(str(collection[l:m+1]) + " and " + str(collection[m+1:r+1]))

    if verbose: print("All sorted.")

    return collection


if __name__ == "__main__":
    from common.invoker import from_input
    from_input(natural_merge_sort)
