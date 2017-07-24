# Calculate lcm of a number.

def gcd(a, b):
    if b==0:
        return a
    return gcd(b, a%b)


def lcm(a, b):
    return a * (b/gcd(a, b))


if __name__ == '__main__':
    assert lcm(10, 4) == 20
