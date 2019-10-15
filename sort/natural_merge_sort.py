"""This module contains natural_merge_sort and other helper functions.

You can run a test using this command:
python3 -m doctest natural_merge_sort.py -v
or just
python3 natural_merge_sort.py [--verbose]
"""

from merge_sort import merge

# Deprecated
def find_two_runs(collection, prev_run_end, until, verbose=False, level=0):
    """Find first two sorted subarray from collection.

    Example:
        >>> find_two_runs([3, 2, 5, 9, 7, 8], 0, 5, False, 0)
        (0, 0, 3)
        >>> find_two_runs([3, 2, 5, 9, 7, 8], 1, 5, False, 0)
        (0, 3, 5)
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


def make_runs(collection):
    """Make list of pair of start/end index of runs.

    Args:
        collection (list): The collection to create runs from.

    Returns:
        list: A list consists of start/end index pair of each runs.

    Example:
        >>> make_runs([8, 9, 6, 7, 3, 4, 1, 5])
        [(0, 1), (2, 3), (4, 5), (6, 7)]
        >>> make_runs([1, 2, 3, 4, 5, 6, 7, 8])
        [(0, 7)]
        >>> make_runs([5, 4, 3, 2, 1])
        [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
        >>> make_runs([1, 2, 3, 5, 4])
        [(0, 3), (4, 4)]
    """

    runs = []
    last_item = collection[0]
    run_start = 0

    for i in range(1, len(collection)):
        if collection[i] < last_item:
            runs.append((run_start, i - 1))
            run_start = i

        if i >= len(collection) - 1:
            runs.append((run_start, len(collection) - 1))

        last_item = collection[i]

    return runs


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

        >>> natural_merge_sort([32, 13, 46, 78, 96, 15, 27])
        [13, 15, 27, 32, 46, 78, 96]
    """

    # natural_merge_sort_recursive(collection, 0, len(collection) - 1, verbose, 0)

    runs = make_runs(collection)

    if verbose:
        print("Initial runs: ", end="")
        [print(collection[run[0]:run[1]+1], end=" ") for run in runs]
        print("")

    while len(runs) > 1:
        i = 0
        merged_runs = []

        if verbose: print("Merge stage " + str(i + 1))

        while i < len(runs):
            # Leave last single item to the next stage.
            if i + 1 >= len(runs):
                merged_runs.append(runs[-1])
                break

            left = runs[i][0]
            middle = runs[i][1]
            right = runs[i + 1][1]

            if verbose:
                print("    Merge "
                + str(collection[left:middle+1])
                + " and "
                + str(collection[middle+1:right+1]))

            merge(collection, left, middle, right)
            merged_runs.append((left, right))

            i += 2

        runs = merged_runs

    return collection


if __name__ == "__main__":
    from common.invoker import from_input
    from_input(natural_merge_sort)
