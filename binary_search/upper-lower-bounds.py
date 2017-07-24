# Find upper and lower bounds of dups in sorted array.
# O(logn) --> with minimum comparisons.

def lower_bound(arr, element):
    left = 0
    right = len(arr)-1

    while left<right:
        mid = left + (right-left)/2  # Saves integer overflow

        if arr[mid]<element:
            left = mid+1
        else:
            right = mid

    return left


def upper_bound(arr, element):
    left = 0
    right = len(arr)-1

    while left<right:
        mid = left + (right-left)/2 + 1  # making right biased

        if arr[mid]>element:
            right = mid-1
        else:
            left = mid
    return right


if __name__ == '__main__':
    assert lower_bound([1, 2, 3, 3, 3, 3, 4, 5], 3) == 2
    assert lower_bound([1, 2, 3, 4, 5, 6, 7, 8, 8], 8) == 7
    assert lower_bound([1, 1, 3, 4, 5, 6, 7, 8, 9], 1) == 0

    assert upper_bound([1, 2, 3, 3, 3, 3, 4, 5], 3) == 5
    assert upper_bound([1, 2, 3, 4, 5, 6, 7, 8, 8], 8) == 8
    assert upper_bound([1, 1, 3, 4, 5, 6, 7, 8, 9], 1) == 1
