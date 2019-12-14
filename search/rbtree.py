"""
Red-black tree implementation.

Not tested yet.
"""

from tree import *


class RBTree:
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


    def insert(self, key_to_insert, verbose=False):
        
        pass
