# Longest common sub sequence - Dynamic solution using bottom up tabulation
# Time O(m*n) and Space O(m*n)

def lcs(pat1, pat2):
    plen1 = len(pat1)
    plen2 = len(pat2)

    mat = [[None]*(plen2+1)]*(plen1+1)

    for i in xrange(plen1+1):
        for j in xrange(plen2+1):
            if i == 0 or j == 0:
                mat[i][j] = 0
            elif pat1[i-1] == pat2[j-1]:
                mat[i][j] = mat[i-1][j-1] + 1
            else:
                mat[i][j] = max(mat[i-1][j], mat[i][j-1])

    return mat[plen1][plen2]

if __name__ == '__main__':
    pat1 = "AGGTAB"
    pat2 = "GXTXAYB"
    print "LCS length: ", lcs(pat1, pat2)
