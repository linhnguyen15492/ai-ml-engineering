def distance(x, origin=[0, 0]):
    if len(x) != 2:
        return "x is not two-dimensional!"
    else:
        return ((x[0] - origin[0]) ** 2 + (x[1] - origin[1]) ** 2) ** 0.5


def in_circle(x, origin=[0, 0]):
    if len(x) != 2:
        return "x is not two-dimensional!"
    elif distance(x, origin) < 1:
        return True
    else:
        return False
