from Tree import Node

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
        # Empty tree has no nodes, neither head.
        self.head = None

    # Tested.
    def is_empty(self):
        return (self.head is None)

    # Tested.
    def equals(self, other):
        this_nodes = list()
        self.dump(visited=this_nodes, verbose=False)

        other_nodes = list()
        other.dump(visited=other_nodes, verbose=False)

        return this_nodes == other_nodes

    def find_node_top_down(self, key_to_find, find_closest=True, verbose=False):
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
        current_node: Node = self.head
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

    # Tested.
    def insert(self, key_to_insert, verbose=False):
        if self.head is None:
            self.head = Node(key=key_to_insert)
            return

        closest_node: Node = self.find_node_top_down(key_to_find=key_to_insert, find_closest=True, verbose=verbose)
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
    def search(self, key_to_find, verbose=False):
        """
        Perform a binary search on this BST.
        Return None if not found.
        """
        if self.is_empty():
            return None

        return self.find_node_top_down(key_to_find=key_to_find, find_closest=False, verbose=verbose)

    # Tested
    def dump(self, root=0, visited=None, verbose=True):
        if root == 0:
            root = self.head

        if root is None:
            return

        if visited is not None and root not in visited:
            # Useful when we want a list of nodes.
            visited.append(root)

        if verbose:
            print(root)

        self.dump(root=root.left, visited=visited, verbose=verbose)
        self.dump(root=root.right, visited=visited, verbose=verbose)

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
        tree1.head = tree1_node5

        tree2 = BinarySearchTree()
        tree2_node9 = Node(9, left=None, right=None)
        tree2_node6 = Node(6, left=None, right=None)
        tree2_node4 = Node(4, left=None, right=None)
        tree2_node2 = Node(2, left=None, right=None)
        tree2_node7 = Node(7, left=tree2_node6, right=tree2_node9)
        tree2_node3 = Node(3, left=tree2_node2, right=tree2_node4)
        tree2_node5 = Node(5, left=tree2_node3, right=tree2_node7)
        tree2.head = tree2_node5

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

        tree.head = node5

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
        tree_by_hand.head = node5

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

        tree.head = node5

        tree.dump()


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
