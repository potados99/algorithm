"""
Binary search tree implementation using linked nodes.

Tested 2019.12.14.
"""

from tree import *

# Tested.
class BinarySearchTree:
    """
    >>> BinarySearchTree.equals_test()
    'Success'

    >>> BinarySearchTree.insert_test()
    'Success'

    >>> BinarySearchTree.search_test()
    'Success'

    >>> BinarySearchTree.dump_test()
    Key: 5, Left: 3, Right: 7.
    Key: 3, Left: 2, Right: 4.
    Key: 2, Left: -, Right: -.
    Key: 4, Left: -, Right: -.
    Key: 7, Left: 6, Right: 9.
    Key: 6, Left: -, Right: -.
    Key: 9, Left: -, Right: -.
    """
    def __init__(self):
        # Empty tree has no nodes, neither root.
        self.root = None

    # Tested.
    def is_empty(self):
        return (self.root is None)

    # Tested.
    def equals(self, other):
        this_nodes = list()
        self.dump(visited=this_nodes, verbose=False)

        other_nodes = list()
        other.dump(visited=other_nodes, verbose=False)

        return this_nodes == other_nodes

    # Tested
    def search(self, key_to_find, verbose=False):
        """
        Perform a binary search on this BST.
        Return None if not found.
        """
        if self.is_empty():
            return None

        return binary_search(root=self.root, key_to_find=key_to_find, find_closest=False, verbose=verbose)

    # Tested.
    def insert(self, key_to_insert, verbose=False):
        if self.root is None:
            self.root = Node(key=key_to_insert)
            return

        closest_node: Node = binary_search(root=self.root, key_to_find=key_to_insert, find_closest=True, verbose=verbose)
        if closest_node is None:
            # No closest node, meaning that there is already a node with the key to insert.
            return

        new_node = Node(key=key_to_insert)
        go_left = (key_to_insert < closest_node.key)

        if go_left:
            closest_node.left = new_node
        else:
            closest_node.right = new_node

    # Tested
    def dump(self, visited=None, verbose=True):
        dump(self.root, visited=visited, verbose=verbose)

    @staticmethod
    def equals_test():
        tree1 = BinarySearchTree()
        tree1_node9 = Node(9, left=None, right=None)
        tree1_node6 = Node(6, left=None, right=None)
        tree1_node4 = Node(4, left=None, right=None)
        tree1_node2 = Node(2, left=None, right=None)
        tree1_node7 = Node(7, left=tree1_node6, right=tree1_node9)
        tree1_node3 = Node(3, left=tree1_node2, right=tree1_node4)
        tree1_node5 = Node(5, left=tree1_node3, right=tree1_node7)
        tree1.root = tree1_node5

        tree2 = BinarySearchTree()
        tree2_node9 = Node(9, left=None, right=None)
        tree2_node6 = Node(6, left=None, right=None)
        tree2_node4 = Node(4, left=None, right=None)
        tree2_node2 = Node(2, left=None, right=None)
        tree2_node7 = Node(7, left=tree2_node6, right=tree2_node9)
        tree2_node3 = Node(3, left=tree2_node2, right=tree2_node4)
        tree2_node5 = Node(5, left=tree2_node3, right=tree2_node7)
        tree2.root = tree2_node5

        return "Success" if tree1.equals(tree2) else "Fail"

    @staticmethod
    def search_test(key_to_find=6):
        tree = BinarySearchTree()

        node9 = Node(9, left=None, right=None)
        node6 = Node(6, left=None, right=None)
        node4 = Node(4, left=None, right=None)
        node2 = Node(2, left=None, right=None)
        node7 = Node(7, left=node6, right=node9)
        node3 = Node(3, left=node2, right=node4)
        node5 = Node(5, left=node3, right=node7)

        tree.root = node5

        result = tree.search(key_to_find)
        return "Success" if result == key_to_find else "Fail"

    @staticmethod
    def insert_test():
        tree = BinarySearchTree()
        tree.insert(5)
        tree.insert(3)
        tree.insert(7)
        tree.insert(2)
        tree.insert(4)
        tree.insert(6)
        tree.insert(9)

        tree_by_hand = BinarySearchTree()
        node9 = Node(9, left=None, right=None)
        node6 = Node(6, left=None, right=None)
        node4 = Node(4, left=None, right=None)
        node2 = Node(2, left=None, right=None)
        node7 = Node(7, left=node6, right=node9)
        node3 = Node(3, left=node2, right=node4)
        node5 = Node(5, left=node3, right=node7)
        tree_by_hand.root = node5

        return "Success" if tree.equals(tree_by_hand) else "Fail"

    @staticmethod
    def dump_test():
        tree = BinarySearchTree()

        node9 = Node(9, left=None, right=None)
        node6 = Node(6, left=None, right=None)
        node4 = Node(4, left=None, right=None)
        node2 = Node(2, left=None, right=None)
        node7 = Node(7, left=node6, right=node9)
        node3 = Node(3, left=node2, right=node4)
        node5 = Node(5, left=node3, right=node7)

        tree.root = node5

        tree.dump()


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
