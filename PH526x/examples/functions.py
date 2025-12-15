def intersect(L1, L2):
    res = []
    for i in L1:
        if i in L2:
            res.append(i)
    return res


# L1 = ['a', 'b', 'c', 'd', 1, 5, 8, 9]
# L2 = [2, 3, 4, 5, 6, 7, 'c', 'd']
# print(intersect(L1, L2))
# print(intersect([1, 2, 3], [3, 4, 5, 6, 7]))


def update(n, x):
    n = 2
    x.append(4)
    print('update: ', n, x)


def main():
    n = 1
    x = [0, 1, 2, 3]
    print('main: ', n, x)
    update(n, x)
    print('main: ', n, x)


main()
