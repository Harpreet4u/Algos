# Calculate square root of N
"""
Babylonian Algorithm:
    (x+S/x)/2
"""


def sqrt(S):
    x = S
    y = 1.
    e = 0.0000001   # Accuracy
    while x-y > e:
        x = (x + y)/2.
        y = S/float(x)
    return x


if __name__ == '__main__':
    assert int(sqrt(16)) == 4
    assert int(sqrt(4)) == 2
