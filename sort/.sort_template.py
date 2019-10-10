"""This module contains a single function: [blahblah].

You can run a test using this command:
    python3 -m doctest [blahblah].py -v
or just
    python3 [blahblah].py [--verbose]
"""


def [blahblah](collection, verbose=False):
    """Implementation of [blahblah] in Python.

    Args:
        collection (list): Input to sort.
        verbose (bool): Print every rotation if true.

    Returns:
        list: The same as the collection, with sort ascending applied.

    Example:
        >>> [blahblah]([3, 1, 7, 0, 4, 8, 2])
        [0, 1, 2, 3, 4, 7, 8]

        >>> [blahblah]([-91, -123, -1])
        [-123, -91, -1]
    """


    return collection


if __name__ == "__main__":
    from common.invoker import from_input
    from_input([blahblah])
