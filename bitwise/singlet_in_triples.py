# All elements occurs three times, except one element, Find that element.
# Complexity: O(n) and space O(1)

"""
Algorithm:

    1. ones -> keep bits appearing 1st time, 4th time....n+3 times
    2. twos -> keep bits appearing 2nd time, 5th time....n+3 times
    3. Throw away bits appearing 3rd time. Which will be common bits of ones and twos

    return ones  --> number appearing ones in equi-triplets.

"""

def find_lonely(arr):
    ones = 0
    twos = 0

    for number in arr:
        twos = twos | (ones & number)
        ones = ones ^ number

        common_mask = ~(ones & twos)
        ones &= common_mask
        twos &= common_mask

    return ones

"""
Modulo Algorithm:

    Take sum of all bits at ones place, tenth place, .... and mod with 3

"""

INT_SIZE = 32

def find_lonely_mod(arr):

    lonely = 0
    for i in xrange(0, INT_SIZE):

        res = 0
        for number in arr:
            res += number&(1<<i)

        if (res%3):
            lonely |= (1<<i)

    return lonely


if __name__ == "__main__":
    assert find_lonely([3, 3, 2, 3]) == 2
    assert find_lonely([3, 3, 2, 3, 2, 1, 2]) == 1

    assert find_lonely_mod([3, 3, 2, 3]) == 2
    assert find_lonely_mod([3, 3, 2, 3, 2, 1, 2]) == 1
    
