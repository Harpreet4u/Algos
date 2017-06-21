# Largest continous sum subarray
# O(n)


def maxSubArraySum(arr, size):
    max_so_far = 0
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + arr[i]
        if max_ending_here < 0:
            max_ending_here = 0
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
    
    return max_so_far

# Another version
def maxSubArraySum2(a, size):
    max_so_far = a[0]
    max_ending_here = a[0]
    for i in range(size):
        max_ending_here = max(a[i], max_ending_here + a[i])
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


