# Run for script only.
from Point import Point

def theta(p0, p1):
    """
    >>> theta(Point(2, 2), Point(5, 5))
    45.0
    >>> theta(Point(5, 5), Point(2, 2))
    225.0
    >>> theta(Point(3, 2), Point(1, 5))
    125.99999999999999
    >>> theta(Point(9, 1), Point(7, 4))
    125.99999999999999
    >>> theta(Point(5, 2), Point(8, 5))
    45.0
    """
    dx = p1.x - p0.x
    dy = p1.y - p0.y
    ax = abs(dx)
    ay = abs(dy)

    atotal = ax + ay
    t = (dy / atotal) if atotal != 0 else 0

    if dx < 0:
        t = 2 - t
    elif dy < 0:
        t = 4 + t

    return t * 90


def package_wrapping(points):
    min_index = points.index(min(points, key=lambda p: p.y))

    angle_min = 0.0
    points.append(points[min_index])
    n = len(points)

    [print((p.x, p.y),end=' ') for p in points]
    print("")

    p = points[min_index]
    points[min_index].shape = '@'

    for sorted_index in range(0, n):
        points[sorted_index], points[min_index] = points[min_index], points[sorted_index]
        angle_last = angle_min
        angle_min = 360.0

        print(str((points[sorted_index].x, points[sorted_index].y)) + " and ", end='')
        for i in range(sorted_index + 1, n):
            print(str((points[i].x, points[i].y)), end=', ')

            angle = theta(points[sorted_index], points[i])
            if angle >= angle_last and angle < angle_min:
                if sorted_index == 0 and i == n - 1:
                    continue
                min_index = i
                angle_min = angle

        print("")

        points[min_index].shape = '@'
        Point.dump_points(points)

        p0 = points[sorted_index]
        p1 = points[min_index]

        print(str(angle_min) + "(" + str((p0.x, p0.y)) + "and" + str((p1.x, p1.y)) + ")" + "\n"*5)

        if min_index == n - 1:
            print("SEX")
            return sorted_index




if __name__ == "__main__":
    import doctest
    doctest.testmod()

    p = Point.create_random_points(size=16, n_points=16)
    m = package_wrapping(p)
