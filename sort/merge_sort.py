"""This module contains three functions: merge_sort, merge_sort_recursive, merge.

You can run a test using this command:
    python3 -m doctest merge_sort.py -v
or just
    python3 merge_sort.py [--verbose]
"""


def merge(collection, left, middle, right, verbose=False, level=0):
    """Merge two sorted subarrays:
    collection[left:middle+1] and collection[middle+1:right+1].

    Args:
        collection (list): The collection that has two sorted subarrays.
        left (int): Start index of left sorted subarray.
        middle (int): End index of left sorted subarray.
        right (int): End index of right sorted subarray.
        verbose (bool): Show steps or not.
        level (int): Indent level. Used to distinguish call depth.

    Return:
        list: The collection, with subbarrays merged.
    """

    left_half = collection[left:middle+1]
    right_half = collection[middle+1:right+1]

    k = left
    l = 0
    r = 0

    # Copy items to collection in ascending order.
    while l < len(left_half) and r < len(right_half):
        if left_half[l] <= right_half[r]:
            collection[k] = left_half[l]
            l += 1
        else:
            collection[k] = right_half[r]
            r += 1
        k += 1
        if verbose: print("    "*level + str(collection[left:k]))

    # Copy remaining items in left half
    while l < len(left_half):
        collection[k] = left_half[l]
        k += 1
        l += 1
        if verbose: print("    "*level + str(collection[left:k]))

    # Copy remaining items in right half
    while r < len(right_half):
        collection[k] = right_half[r]
        k += 1
        r += 1
        if verbose: print(collection[left:k])

    if verbose: print("    "*level + "Merged: " + str(collection[left:right+1]))

    return collection


def merge_sort_recursive(collection, left, right, verbose=False, level=0):
    """Merge sort implementation in recursive way.

        Args:
            collection (list): The collection to sort.
            left (int): Most left index of collection to sort.
            right (int): Most right index of collection to sort.
            verbose (bool): Print steps or not.
            level (int): Indent level. Used to distinguish call depth.

        Returns:
            list: The sorted collection.

        Example:
            >>> merge_sort_recursive([4, 7, 8, 2, 5], 0, 4, False)
            [2, 4, 5, 7, 8]
            >>> merge_sort_recursive([9, 8, 7, 6, 5, 4, 3, 2, 1], 0, 3, False)
            [6, 7, 8, 9, 5, 4, 3, 2, 1]
    """

    if left >= right:
        return collection

    middle = left + ((right - left) >> 1)

    if verbose:
        print("    "*level
        + "1. Left: "
        + str(collection[left:middle+1]))
    merge_sort_recursive(collection, left, middle, verbose, level + 1)

    if verbose:
        print("    "*level
        + "2. Right: "
        + str(collection[middle+1:right+1]))
    merge_sort_recursive(collection, middle + 1, right, verbose, level + 1)

    if verbose:
        print("    "*level
        + "3. Merge: "
        + str(collection[left:middle+1])
        + " and "
        + str(collection[middle+1:right+1]))
    merge(collection, left, middle, right, verbose, level + 1)

    return collection


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

    merge_sort_recursive(collection, 0, len(collection) - 1, verbose, 0)

    return collection


if __name__ == "__main__":
    from common.invoker import from_input
    from_input(merge_sort)
