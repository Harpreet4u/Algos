# http://www.geeksforgeeks.org/recursively-break-number-3-parts-get-maximum-sum/
# Recursive calculations or use DP

def g(n):
    if n == 0:
        return 0
    return int(max(n, g(n/2)+g(n/3)+g(n/4)))

print g(int(raw_input()))
