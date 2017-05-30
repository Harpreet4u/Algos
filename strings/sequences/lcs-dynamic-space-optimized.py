# Longest Common sub sequence - dynamic solution - space optimized
# Time O(m*n) and Space O(n)

def lcs(pat1, pat2):
    plen1 = len(pat1)
    plen2 = len(pat2)

    mat = [[None]*(plen2+1)]*2

    row = 0
    for i in xrange(plen1+1):
        row = i&1
        for j in xrange(plen2+1):
            if i == 0 or j == 0:
                mat[row][j] = 0
            elif pat1[i-1] == pat2[j-1]:
                mat[row][j] = mat[1-row][j-1] + 1
            else:
                mat[row][j] = max(mat[row][j-1], mat[1-row][j])
    return mat[row][plen2]

if __name__ == '__main__':
    pat1 = "AGGTAB"
    pat2 = "GXTXAYB"
    print "LCS length: ", lcs(pat1, pat2)
