class TreeUtil:
    """
    Useful methods for tree indexing in array(list) organization.
    """
    @staticmethod
    def left(root: int):
        """
        >>> Tree.left(0)
        1
        >>> Tree.left(1)
        3
        >>> Tree.left(3)
        7
        """
        return (root << 1) + 1

    @staticmethod
    def right(root: int):
        """
        >>> Tree.right(0)
        2
        >>> Tree.right(1)
        4
        >>> Tree.right(3)
        8
        """
        return (root << 1) + 2

    @staticmethod
    def parent(child: int):
        """
        >>> Tree.parent(3)
        1
        >>> Tree.parent(4)
        1
        >>> Tree.parent(2)
        0
        """
        return (child - 1) >> 1


class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __str__(self):
        left = str(self.left.key) if self.left is not None else "-"
        right = str(self.right.key) if self.right is not None else "-"
        return "Key: " + str(self.key) + ", Left: " + left + ", Right: " + right + "."

    def __eq__(self, other):
        if type(self) != type(other):
            # Only accepts same type.
            return False

        return ((self.key == other.key)
        and ((self.left.key if self.left is not None else None) == (other.left.key if other.left is not None else None))
        and ((self.right.key if self.right is not None else None) == (other.right.key if other.right is not None else None)))

    def __hash__(self):
        return hash(('key', self.key, 'left', self.left.key if self.left is not None else None, 'right', self.right.key if self.right is not None else None))
