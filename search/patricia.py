"""
Patricia Tree implementation.

Tested 2019.12.13.
"""

# Tested.
class Bitskey:
    def __init__(self, val: int):
        self.val: int = val

    def get(self):
        return self.val

    def bits(self, offset: int, mask: int=1):
        """
        Return 'mask' bits at 'offset' away from LSB.
        >>> Bitskey(5).bits(2, 1)
        1
        >>> Bitskey(15).bits(2, 2)
        3
        """
        return (self.val >> offset) & ~(~0 << mask)

    def cmp(self, offset: int, operand: int):
        """
        Compare a bit at 'offset'(from LSB) with 'operand'.
        """
        return self.bits(offset, 1) == operand

    def __str__(self):
        return str(self.val)

    def __eq__(self, other):
        return self.val == other.val

    def __hash__(self):
        return hash(('val', self.val))


# Tested.
class Node:
    def __init__(self, key: Bitskey, left=None, right=None, skipped_bit: int=0):
        self.key: Bitskey = key
        self.left: Node = left if left is not None else self
        self.right: Node = right if right is not None else self
        self.skipped_bit: int = skipped_bit

    def __str__(self):
        left = str(self.left.key) if self.left is not None else "-"
        right = str(self.right.key) if self.right is not None else "-"

        return "Key: " + str(self.key) + ", Skipped bit: " + str(self.skipped_bit) + ", Left: " + left + ", Right: " + right + "."


# Tested.
class Patricia:
    """
    >>> Patricia.search_test(26)
    'Success'
    >>> Patricia.insert_test()
    Key: 19, Skipped bit: 4, Left: 9, Right: 26.
    Key: 9, Skipped bit: 3, Left: 5, Right: 9.
    Key: 5, Skipped bit: 2, Left: 3, Right: 5.
    Key: 3, Skipped bit: 1, Left: 1, Right: 3.
    Key: 1, Skipped bit: 0, Left: 1, Right: 1.
    Key: 26, Skipped bit: 3, Left: 18, Right: 26.
    Key: 18, Skipped bit: 0, Left: 18, Right: 19.
    """
    def __init__(self):
        self.key_min: Bitskey = Bitskey(-1)
        self.root: Node = Node(self.key_min)

    def is_empty(self):
        return self.root.key == self.key_min

    def select_child(self, key_to_find: Bitskey, parent: Bitskey, verbose=False):
        """
        Select a child node given key and the offset of the parent node.
        """
        if key_to_find.cmp(offset=parent.skipped_bit, operand=1):
            if verbose: print("Go right.")
            selected = parent.right
        else:
            if verbose: print("Go left.")
            selected = parent.left

        if verbose:
            print("")
            print("[Parent] " + str(parent))
            print("[Child] " + str(selected))

        return selected

    def find_node_top_down(self, key_to_find: Bitskey, until: int=-1, verbose=False):
        """
        Find node that contains 'key_to_find'.
        If failed, it returns a closest node.
        We can limit the skipped bit using 'until'.
        """
        parent: Node = self.root
        child: Node = self.select_child(key_to_find=key_to_find, parent=parent, verbose=verbose)

        while parent.skipped_bit > child.skipped_bit and child.skipped_bit > until:
            parent = child

            if verbose:
                print("Step down to next level.")
                print("Skipped bit is at " + str(child.skipped_bit) + ".")

            child = self.select_child(key_to_find=key_to_find, parent=child, verbose=verbose)

        return (parent, child)

    def find_closest_node(self, key_to_find: Bitskey, verbose=False):
        """
        Find the closest node, the last node visited when search is failed.
        """
        node: Node = self.find_node_top_down(key_to_find=key_to_find, verbose=verbose)[1]
        return node if node.key != key_to_find else None

    def find_proper_parent_and_child(self, key_to_find: Bitskey, skipped_bit: int, verbose=False):
        """
        Find a proper node that should be a child node for a new node of key 'key_to_find'.
        """
        return self.find_node_top_down(key_to_find=key_to_find, until=skipped_bit, verbose=verbose)

    def search(self, key_to_find: Bitskey, for_insert=False, verbose=False):
        """
        Perform a search using key.

        Params:
            key_to_find(Bitskey): A key to find in a tree(trie).

        Returns:
            Bitskey: Matching key on success, minimum key on failure.
        """
        node: Node = self.find_node_top_down(key_to_find=key_to_find, verbose=verbose)[1]

        if key_to_find == node.key:
            if verbose: print("The key(" + str(key_to_find) + ") is found.")
            return node.key
        else:
            if verbose: print("The key(" + str(key_to_find) + ") is not found.")
            return self.key_min

    def insert(self, key_to_insert: Bitskey, max_width=14, verbose=False):
        if self.is_empty():
            # First time insert.
            skipped_bit = max_width
            while key_to_insert.cmp(skipped_bit, 0): skipped_bit -= 1

            self.root = Node(key=key_to_insert, skipped_bit=skipped_bit)

            return

        # Check if it exists.
        closest_node: Node = self.find_closest_node(key_to_find=key_to_insert, verbose=verbose)
        if closest_node is None: return

        # Find proper skipped_bit for the new key.
        skipped_bit = max_width
        while closest_node.key.cmp(skipped_bit, 1) == key_to_insert.cmp(skipped_bit, 1):
            skipped_bit -= 1

        # Find proper parent and child. The new node will be between them.
        parent, child = self.find_proper_parent_and_child(key_to_find=key_to_insert, skipped_bit=skipped_bit, verbose=verbose)

        # Create new node.
        new_node: Node = Node(key=key_to_insert, skipped_bit=skipped_bit)

        # Set direction of the child node.
        if key_to_insert.cmp(new_node.skipped_bit, 1):
            new_node.left = child
        else:
            new_node.right = child

        # Set direction of the new node.
        parent_and_child_are_root = (parent == child and child == self.root)
        root_will_be_chagned = (new_node.skipped_bit > self.root.skipped_bit)

        if parent_and_child_are_root and root_will_be_chagned:
            # Do nothing. It happens on the second insertion.
            pass
        else:
            if key_to_insert.cmp(parent.skipped_bit, 1):
                parent.right = new_node
            else:
                parent.left = new_node

        # Update rooter if new node becomes root.
        if root_will_be_chagned:
            self.root = new_node

    def dump(self, root=None, visited=[]):
        if root in visited:
            return

        if root is None:
            root = self.root

        print(root)
        visited.append(root)

        if root.left != root:
            self.dump(root.left)
        if root.right != root:
            self.dump(root.right)

    @staticmethod
    def search_test(key_to_find=3):
        dict: Patricia = Patricia()

        # As same as the textbook.
        node1: Node = Node(key=Bitskey(1), skipped_bit=0)
        node18: Node = Node(key=Bitskey(18), skipped_bit=0)
        node3: Node = Node(key=Bitskey(3), left=node1, skipped_bit=1)
        node26: Node = Node(key=Bitskey(26), left=node18, skipped_bit=3)
        node5: Node = Node(key=Bitskey(5), left=node3, skipped_bit=2)
        node19: Node = Node(key=Bitskey(19), left=node5, right=node26, skipped_bit=4)

        dict.root = node19
        dict.key_min = Bitskey(1)

        result: Bitskey = dict.search(Bitskey(key_to_find), verbose=False)

        if result.get() == key_to_find:
            return "Success"
        else:
            return "Fail"

    @staticmethod
    def insert_test():
        dict: Patricia = Patricia()

        dict.insert(Bitskey(1))
        dict.insert(Bitskey(19))
        dict.insert(Bitskey(5))
        dict.insert(Bitskey(18))
        dict.insert(Bitskey(3))
        dict.insert(Bitskey(26))
        dict.insert(Bitskey(9))

        dict.dump()


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
