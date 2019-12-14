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
    def is_empty():
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

    def split(self):
        pass


    


    def insert(self, key_to_insert, verbose=False):
        if self.is_empty():
            self.root = RBNode(key=key_to_insert, color=RED)
            return

        closest: Node = binary_search(root=self.root, key_to_find=key_to_insert, find_closest=True, verbose=verbose)
        if closest is None:
            # Already exists.
            return




        pass

    # Tested.
    def dump(self, visited=None, verbose=True):
        dump(self.root, visited=visited, verbose=verbose)

    @staticmethod
    def insert_test():
        pass
