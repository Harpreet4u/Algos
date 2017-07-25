# Longest Palindromic sub-sequence
# O (n^2) and n^2 space dynamic algo

def longest_palindromic_subsequence(string):
    T = [[0]*len(string)]*len(string)

    for i in xrange(len(string)):
        T[i][i] = 1

    for l in xrange(2, len(string)+1):
        for i in xrange(len(string)-l+1):
            j = i+l-1
            if l == 2 and string[i] == string[j]:
                T[i][j] = 2
            elif string[i] == string[j]:
                T[i][j] = T[i+1][j-1] + 2
            else:
                T[i][j] = max(T[i][j-1], T[i+1][j])

    return T[0][len(string)-1]


if __name__ == '__main__':
    assert longest_palindromic_subsequence('agbdba') == 5
