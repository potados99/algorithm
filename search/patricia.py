class Bitskey:
    def __init__(self, val):
        # The key itself.
        self.val = val

    def get(self):
        return self.val

    def bits(self, offset, mask=1):
        """
        Return 'mask' bits at 'offset' away from LSB.
        >>> Bitskey(5).bits(2, 1)
        1
        >>> Bitskey(15).bits(2, 2)
        3
        """
        return (self.val >> offset) & ~(~0 << mask)


class Node:
    def __init__(self, key):
        self.key = key



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
