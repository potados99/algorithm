"""This module contains tournament_sort and other helper functions.

You can run a test using this command:
python3 -m doctest tournament_sort.py -v
or just
python3 tournament_sort.py [--verbose]
"""


# This module can be executed as module and script and by doctest.
if __name__ == "__main__" or __name__ == "tournament_sort":
    from common.util import *
else:
    from .common.util import *


def match(collection, left, right):
    """Match two players.

    The smaller one wins.

    Args:
        collection (list): List of players.
        left (int): Index of left player.
        right (int): Index of right player.

    Returns:
        int: Index of the winner.
        The smaller one wins the match.
        If two are same, the player at left wins.
        Return nothing when collection is empty.

    Example:
        >>> match([4,1,3,2,5], 1, 2)
        1
        >>> match([], 2, 3)
        >>> match([1, 1], 0, 1)
        0
    """

    if len(collection) == 0:
        return

    if collection[left] <= collection[right]:
        return left
    else:
        return right


def run_tournament(collection, start, end):
    """Run match among all players in collection and get the final winner.
    Simply saying it returns the index of the minimum value is the collection.

    This function does not modify collection. It only derefers collection to
    run a match: like comparing player at index 0 and other one at index 1.

    Arg:
        collection (list): Collection of players to run matches.
        start (int): Start index of collection to run matches.
        end (int): Last index of collection to run matches.
        verbose (bool): To print steps or not.

    Returns:
        int: Index of minimum value(winner) in collection.

    Example:
        >>> run_tournament([9, 5, 3, 6, 1, 4], 0, 5)
        4
        >>> run_tournament([9, 5, 3, 6, 1, 4], 0, 3)
        2
        >>> run_tournament([1, 1, 1, 1], 0, 3)
        0
        >>> run_tournament([-1, -3, -2], 0, 2)
        1
    """

    if len(collection) == 0 or end < start:
        return

    player_indices = list(range(0, len(collection)))[start:end+1]

    while len(player_indices) > 1:
        # Pop two.
        player_right = player_indices.pop()
        player_left = player_indices.pop()

        # Compare them.
        winner = match(collection, player_left, player_right)

        # Push the winner
        player_indices.insert(0, winner)

    return player_indices.pop()


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

    for i in range(0, len(collection) - 1):
        if verbose: print("Rotation " + str(i + 1))

        if verbose: print("    Run tournament from " + str(collection[i:len(collection)]))
        min_index = run_tournament(collection, i, len(collection) - 1)
        if verbose: print("    The winner is " + str(collection[min_index]))

        swap(collection, i, min_index)
        if verbose: print("    Place " + str(collection[min_index]) + " at index " + str(i))
        if verbose: print(collection)

    return collection


if __name__ == "__main__":
    from common.invoker import from_input
    from_input(tournament_sort)
