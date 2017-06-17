
def nCr(n, r):
    res = 1

    if r > n-r:
        r = n-r
    for i in xrange(r):
        res *= (n-i)
        res /= (i+1)
    return res

if __name__ == '__main__':
    print nCr(2, 1)
    assert nCr(2, 1) == 2
    
    print nCr(4, 2)
    assert nCr(4, 2) == 6
