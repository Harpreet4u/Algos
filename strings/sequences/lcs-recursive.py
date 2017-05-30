# Longest common sub sequence - recursive naive solution
# O(2^n) -- Overlapping sub problem in recursion tree

def lcs(pat1, pat2, plen1, plen2):
    if plen1 == 0 or plen2 == 0:
        return 0
    elif pat1[plen1-1] == pat2[plen2-1]:
        return 1 + lcs(pat1, pat2, plen1-1, plen2-1)
    else:
        return max(lcs(pat1, pat2, plen1-1, plen2), lcs(pat1, pat2, plen1, plen2-1))

if __name__ == '__main__':
    pat1 = "AGGTAB"
    pat2 = "GXTXAYB"
    print "LCS length: ", lcs(pat1, pat2, len(pat1), len(pat2))
