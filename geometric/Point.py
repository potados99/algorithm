import random
import itertools


class Point:
    """
    2D point.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shape = '*'

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == self.y)

    def __hash__(self):
        return hash(('x', self.x, 'y', self.y))

    @staticmethod
    def create_random_points(size, n_points):
        points = list()
        for i in range(0, n_points):
            x = int(random.randint(0, size - 1))
            y = int(random.randint(0, size - 1))
            p = Point(x, y)
            points.append(p)

        # No duplicates.
        return list(set(points))

    @staticmethod
    def dump_points(m, width=2):
        y_sorted = sorted(m, key=lambda p: p.y)
        y_indices = list(set(map(lambda p: p.y, y_sorted))) # y dups killed.
        splited = [list(filter(lambda p: p.y == y, y_sorted)) for y in y_indices]
        processed = [sorted(list(set(l)), key=lambda p: p.x) for l in splited] # x dups killed.

        y_offset = 0
        x_offset = 0

        for row in processed:
            y = row[0].y
            to_go = y - y_offset
            print('\n'*to_go, end='')
            y_offset = y
            x_offset = 0

            for p in row:
                x = p.x
                to_go = x - x_offset - 1
                print(' '*(width*to_go), end='')
                x_offset = x
                print(str(p.shape) + ' '*(width-1), end='')

        print("")
