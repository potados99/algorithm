"""
Some helpful things for tree implementation.

Tested 2019.12.14.
"""

# Tested.
class Node:
    """
    >>> Node(3) == Node(3)
    True
    >>> str(Node(4))
    'Key: 4, Left: -, Right: -.'
    """
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


# Tested.
class RBNode(Node):
    """
    >>> RBNode(3, color=RBNode.BLACK) == RBNode(3, color=RBNode.BLACK)
    True
    >>> str(RBNode(3, color=RBNode.BLACK))
    'Key: 3, Color: BLACK, Left: -, Right: -.'
    """
    BLACK = 0
    RED = 1

    def __init__(self, key, color=BLACK, left=None, right=None):
        Node.__init__(self, key=key, left=left, right=right)
        self.color = color

    def __str__(self):
        color = "BLACK" if self.color == self.BLACK else "RED"
        left = str(self.left.key) if self.left is not None else "-"
        right = str(self.right.key) if self.right is not None else "-"
        return "Key: " + str(self.key) + ", Color: " + color + ", Left: " + left + ", Right: " + right + "."

    def __eq__(self, other):
        if type(self) != type(other):
            # Only accepts same type.
            return False

        return Node.__eq__(self, other) and self.color == other.color

    def __hash__(self):
        return hash(('key', self.key, 'color', self.color, 'left', self.left.key if self.left is not None else None, 'right', self.right.key if self.right is not None else None))


#Tested.
def left(root: int):
    """
    >>> TreeUtil.left(0)
    1
    >>> TreeUtil.left(1)
    3
    >>> TreeUtil.left(3)
    7
    """
    return (root << 1) + 1


#Tested.
def right(root: int):
    """
    >>> TreeUtil.right(0)
    2
    >>> TreeUtil.right(1)
    4
    >>> TreeUtil.right(3)
    8
    """
    return (root << 1) + 2


#Tested.
def parent(child: int):
    """
    >>> TreeUtil.parent(3)
    1
    >>> TreeUtil.parent(4)
    1
    >>> TreeUtil.parent(2)
    0
    """
    return (child - 1) >> 1


# Tested.
def binary_search(root: Node, key_to_find, find_closest=True, verbose=False):
        """
        Perform a binary search from root node.

        Params:
            key_to_find (comparable): A key to find in the tree.
            find_closest (bool): Return the closest node if search failed.

        Returns:
            if key found and find_closest: the node.
            if key found and not find_closest: None.
            if key not found and find_closest: the closest node.
            if key not found and not find_closest: None.

        """
        current_node: Node = root
        last_node: Node = None

        while current_node is not None:
            if current_node.key == key_to_find:
                return key_to_find

            # In this BST implementation, nodes who are smaller than the key
            # goes left, and those equal to or bigger than the key goes right.
            go_left = (key_to_find < current_node.key)

            last_node = current_node
            current_node = current_node.left if go_left else current_node.right

        if current_node is None:
            # Not found
            return last_node if find_closest else None
        else:
            # Found
            return None if find_closest else current_node


# Tested
def dump(root, visited=None, verbose=True):
    if root is None:
        return

    if visited is not None and root not in visited:
        # Useful when we want a list of nodes.
        visited.append(root)

    if verbose:
        print(root)

    dump(root=root.left, visited=visited, verbose=verbose)
    dump(root=root.right, visited=visited, verbose=verbose)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
