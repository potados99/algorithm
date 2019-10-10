"""This module contains a single function: cocktail_shaker.

You can run a test using this command:
python3 -m doctest cocktail_shaker.py -v
or just
python3 cocktail_shaker.py [--verbose]
"""


def cocktail_shaker(collection, verbose=False):
    """Implementation of cocktail shaker in Python.

    Args:
        collection (list): Input to sort.
        verbose (bool): Print every rotation if true.

    Returns:
        list: The same as the collection, with sort ascending applied.

    Example:
        >>> cocktail_shaker([3, 1, 7, 0, 4, 8, 2])
        [0, 1, 2, 3, 4, 7, 8]

        >>> cocktail_shaker([-91, -123, -1])
        [-123, -91, -1]
    """

    size = len(collection)
    direction = True # To right

    left = 0
    right = size - 1

    for i in range(0, (size >> 1) + 1):
        if direction:
            if verbose: print("To right!")
            for j in range(left, size - 1): # 0 to size -1
                if collection[j] > collection[j + 1]:
                    collection[j], collection[j + 1] = collection[j + 1], collection[j]
                    if verbose: print(collection)
            right -= 1

        else:
            if verbose: print("To left!")
            for j in range(right, 0, -1): # size - 1 to 1
                if collection[j - 1] > collection[j]:
                    collection[j - 1], collection[j] = collection[j], collection[j - 1]
                    if verbose: print(collection)
            left += 1

        if right - left <= 1: break

        direction = not direction

    return collection


if __name__ == "__main__":
    from invoker import from_input
    from_input(cocktail_shaker)
