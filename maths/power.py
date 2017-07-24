# Calculate x^y iterative one
# O(logn)


def pow(x, y):
    res = 1

    while y > 0:
        if y&1:
            res = res*x
        y >>= 1
        x *= x

    return res


if __name__ == '__main':
    assert pow(2, 3) == 8
    assert pow(2, 10) == 1024
    assert pow(3, 4) == 81
