# https://www.hackerrank.com/challenges/array-left-rotation

n, r = map(int, raw_input().strip().split())
arr = map(int, raw_input().strip().split())

def reverse(arr, l, r):
    mid = (r-l)/2
    for i in xrange(mid+1):
        arr[l+i], arr[r-i] = arr[r-i], arr[l+i] 

def left_rotate(arr, k):
    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)
    reverse(arr, 0, n-1)
    return arr

print " ".join(map(str, left_rotate(arr, r)))
