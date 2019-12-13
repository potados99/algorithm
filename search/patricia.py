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


class Node:
    def __init__(self, key: Bitskey, left=None, right=None, skipped_bit: int=0):
        self.key: Bitskey = key
        self.left: Node = left if left is not None else self
        self.right: Node = right if right is not None else self
        self.skipped_bit: int = skipped_bit

    def __str__(self):
        return "Key: " + str(self.key) + ", Skipped bit: " + str(self.skipped_bit) + "."


class Dict:
    """
    >>> Dict.search_test(26)
    'Success'

    """
    def __init__(self):
        self.key_min: Bitskey = Bitskey(0)
        self.head: Node = Node(self.key_min)

        self.head.skipped_bit = 14
        self.head.left = self.head
        self.head.right = self.head

    def select_child(self, key_to_find: Bitskey, parent: Bitskey, verbose=False):
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

    def search(self, key_to_find: Bitskey, verbose=False):
        parent: Node = self.head
        child: Node = self.head.left

        child = self.select_child(key_to_find, parent)

        while parent.skipped_bit > child.skipped_bit:
            parent = child

            if verbose:
                print("Step down to next level.")
                print("Skipped bit is at " + str(child.skipped_bit) + ".")

            child = self.select_child(key_to_find=key_to_find, parent=child)

        if key_to_find == child.key:
            if verbose: print("The key(" + str(key_to_find) + ") is found.")
            return child.key
        else:
            if verbose: print("The key(" + str(key_to_find) + ") is not found.")
            return self.key_min

    def insert(self, key: Bitskey, verbose=False):
        print("Insert called!")
        # Check if it exists
        result: Bitskey = self.search(key)
        print(result)
        if result.get() == key.get():
            # Already exists!
            print("Already here!")
            return
        pass

    @staticmethod
    def search_test(key_to_find=3):
        dict: Dict = Dict()

        # As same as the textbook.
        node1: Node = Node(key=Bitskey(1), skipped_bit=0)
        node18: Node = Node(key=Bitskey(18), skipped_bit=0)
        node3: Node = Node(key=Bitskey(3), left=node1, skipped_bit=1)
        node26: Node = Node(key=Bitskey(26), left=node18, skipped_bit=3)
        node5: Node = Node(key=Bitskey(5), left=node3, skipped_bit=2)
        node19: Node = Node(key=Bitskey(19), left=node5, right=node26, skipped_bit=4)

        dict.head = node19
        dict.key_min = Bitskey(1)

        result: Bitskey = dict.search(Bitskey(key_to_find), verbose=True)

        #dict.insert(Bitskey(26))

        if result.get() == key_to_find:
            return "Success"
        else:
            return "Fail"

    @staticmethod
    def insert_test():
        return "NotImplemented"


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
