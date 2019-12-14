"""
Red-black tree implementation.

Not tested yet.
"""

from tree import *


class RBTree:
    """
    >>> insert_test()

    """
    def __init__(self):
        self.root = None

    # Tested.
    def is_empty(self):
        return (self.root is None)

    # Tested.
    def search(self, key_to_find, verbose=False):
        """
        Perform a binary search on this RB tree.
        Return None if not found.
        """
        if self.is_empty():
            return None

        return binary_search(root=self.root, key_to_find=key_to_find, find_closest=False, verbose=verbose)


    def rotate(self):
        pass

    def split(self, root: Node, verbose=False):
        """
        Bottom up, recursively.
        """
        if root is None:
            return
        if root.left is None or root.right is None:
            return

        if root.left.color == RBNode.RED and root.right.color == RBNode.RED:
            # If two child nodes are red, make them BLACK and parent node RED.
            root.color = RBNode.RED
            root.left.color = RBNode.BLACK
            root.right.color = RBNode.BLACK

            # This change may affect other nodes(such as uncle).
            # So do this thing recursively from bottom to top.
            self.split(root.parent)

    def insert(self, key_to_insert, verbose=False):
        if self.is_empty():
            # Empty?
            self.root = RBNode(key=key_to_insert, color=RBNode.BLACK)
            return

        closest: Node = binary_search(root=self.root, key_to_find=key_to_insert, find_closest=True, verbose=verbose)
        if closest is None:
            # Already exists?
            return

        # Just insert first.
        new_node = RBNode(key=key_to_insert, color=RBNode.RED, parent=closest)
        go_left = (key_to_insert < closest.key)

        if go_left: closest.left = new_node
        else: closest.right = new_node

        # Check if we have to do something.
        



    # Tested.
    def dump(self, visited=None, verbose=True):
        dump(self.root, visited=visited, verbose=verbose)

    @staticmethod
    def insert_test():
        pass


if __name__ == "__main__":
    tree = RBTree()

    tree.insert(1)
    tree.insert(8)
    tree.dump()
