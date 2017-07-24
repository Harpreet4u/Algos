# Count inversions in an array
# O(nlogn)  mergesort algo


def merge(A, B):
    M = []
    cnt = 0

    while A and B:
        if A[0]<=B[0]:
            M.append(A.pop(0))
        else:
            M.append(B.pop(0))
            cnt += len(A)
    M += A+B
    return M, cnt

def mergesort(A):
    l = len(A)
    if l>1:
        mid = l/2
        B, b = mergesort(A[:mid])
        C, c = mergesort(A[mid:])
        D, d = merge(B, C)
        return D, b+c+d
    return A, 0


if __name__ == '__main__':
    assert mergesort([2, 3, 1, 4, 5]) == 2
    assert mergesort([2, 4, 1, 3, 5]) == 3
