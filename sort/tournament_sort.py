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

from collections import deque
from math import *


def left_child(collection, node):
    return (2 * node) - len(collection) - 1


def right_child(collection, node):
    return (2 * node) - len(collection)


def parent(collection, node):
    return (node + len(collection) + 1) // 2


def match(collection, left, right, index_mapper=lambda x: x):
    """Compare and return the winner.

    The small one wins. If same, the left wins.
    If one is None, the other one wins.
    If both are None, the winner is None.

    Args:
        collection (list): A collection that contains players.
        left (int): Index of a player at left.
        right (int): Index of a player at right.

    Returns:
        int: Index of the winner in the collection.

    Example:
        >>> match([1, 2, 3, 4], 1, 3, lambda x: [4, 3, 2, 1][x])
        1
        >>> match([1, 1, 1, 1], 0, 3, lambda x: [2, 2, 2, 2][x])
        2
    """

    left = index_mapper(left)
    right = index_mapper(right)

    if left is None and right is None:
        return None
    elif left is None:
        return right
    elif right is None:
        return left

    return left if collection[left] <= collection[right] else right


def print_tournament_tree(collection, tree):
    if len(collection) == 0:
        print("Tree empty.")
        return

    line_capacity = 1
    line_count = 0
    padding = 2**ceil(log2(len(tree)))

    for tree_index in range(len(tree) - 1, -1, -1):
        element = "*" if tree[tree_index] is None else str(collection[tree[tree_index]])
        print_padding(element, padding, end="")

        line_count += 1
        if line_count >= line_capacity:
            print("")
            padding //= 2
            line_capacity *= 2
            line_count = 0


def construct_tournament_tree(collection):
    """Build a tournament tree from given items in collection.
    This function modifies the collection.

    The tree will be represented in a list, from the leafs, not the root.
    Like: [2, 1, 3, *, 5, 6, 7] represents
                7
        5               6
    2       1       3       *

    In this representation the index of the left child is (2i - l - 1),
    where l is total heap size, and that of the right child is (2i - l).
    The index of the parent node will be (i + i) / 2.

    Args:
        collection (list): Initial data. They will not be modified.

    Returns:
        list: A Tournament tree where each node holds item index of
        original collection.

    Example:
        >>> construct_tournament_tree([2, 1, 3, 8, 5, 6, 7])
        [0, 1, 2, 3, 4, 5, 6, None, 1, 2, 4, 6, 1, 4, 1]

        >>> construct_tournament_tree([5, 4, 3, 2, 1])
        [0, 1, 2, 3, 4, None, None, None, 1, 3, 4, None, 3, 4, 4]
    """

    if len(collection) == 0:
        return [None]

    # Get nearst 2^k >= len(collection), where k is integer.
    designated_leaf_count = 2**ceil(log2(len(collection)))

    # The size of the tree will be 2 * designated_leaf_count - 1.
    heap_size = (designated_leaf_count * 2) + 1

    # Indices of the collection.
    indices = list(range(0, len(collection)))

    # Empty part of leaf level.
    padding = [None] * (designated_leaf_count - len(collection))

    # A tree taht will be used as a tournament tree.
    # Every element will hold a key to an element,
    # which is the index of the item in collection.
    tree = indices + padding

    for i in range(0, heap_size - 3, 2):
        winner = match(collection, i, i + 1, index_mapper=lambda x: tree[x])
        tree.append(winner)

    return tree


def retrace_tournament_tree(collection, tree, node):
    """Run a partial rematch from specific node to the root.

    Run a match beteen left child of node and right one of it.
    Do it recursively until it gets to the root.

    Args:
        collection (list): Original data to refer.
        tree (list): A tournament tree.
        node (int): Index of node in the tree.

    Returns:
        list: Retraced tournament tree. The tree modified.

    Example:
        >>> retrace_tournament_tree([2, 1, 3, 8, 5, 6, 7], [0, None, 2, 3, 4, 5, 6, None, 1, 2, 4, 6, 1, 4, 1], 1)
        [0, None, 2, 3, 4, 5, 6, None, 0, 2, 4, 6, 0, 4, 0]
    """


    # Do when node is not a leaf node.
    if node > (len(tree) // 2):
        left = left_child(tree, node)
        right = right_child(tree, node)

        winner = match(collection, left, right, index_mapper=lambda x: tree[x])
        tree[node] = winner

    if node < len(tree) - 1:
        return retrace_tournament_tree(collection, tree, parent(tree, node))
    else:
        return tree


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

    output = []
    tree = construct_tournament_tree(collection)

    if verbose:
        print("Tournament tree constructed:")
        print_tournament_tree(collection, tree)
        print("")

    # Root of the tree points to the minumum value in the collection.
    winner_index = tree[-1]

    while winner_index is not None:
        if verbose:
            print("Run tournament.")
            print("Winner is " + str(collection[winner_index]) + ".")
            print("The tree looks like:")
            print_tournament_tree(collection, tree)
            print("")

        # Add winner to the output.
        output.append(collection[winner_index])

        # The winner_index is not only an index of collection,
        # but also an index of the tree.
        # It is possible to locate index of the winner in the tree
        # because the winner comes from the leaf and the leafs form
        # a range from 0 to len(collection) - 1.
        # Unless the root is None, we can figure out where the winner came from.
        tree[winner_index] = None
        retrace_tournament_tree(collection, tree, winner_index)

        winner_index = tree[-1]

    return output


if __name__ == "__main__":
    from common.invoker import from_input
    from_input(tournament_sort)
