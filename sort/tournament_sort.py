"""This module contains a single function: tournament_sort.

You can run a test using this command:
python3 -m doctest tournament_sort.py -v
or just
python3 tournament_sort.py [--verbose]
"""


def tournament_sort(collection, verbose=False):
    """Implementation of tournament sort in Python.

    Args:
        collection (list): Input to sort.
        verbose (bool): Print every rotation if true.

    Returns:
        list: The same as the collection, with sort ascending applied.

    Example:
        >>> tournament_sort([3, 1, 7, 0, 4, 8, 2])
        [0, 1, 2, 3, 4, 7, 8]

        >>> tournament_sort([-91, -123, -1])
        [-123, -91, -1]

        >>> tournament_sort([])
        []
    """


    return collection


if __name__ == "__main__":
    from common.invoker import from_input
    from_input(tournament_sort)
