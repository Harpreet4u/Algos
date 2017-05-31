# Longest Common SubString - recursive implementation
# O(2^N) Exponentional

def lcs(pat1, pat2, plen1, plen2, check):
    if plen1 == 0 or plen2 == 0:
        return 0
    if check:
        if pat1[plen1-1] == pat2[plen2-1]:
            return 1 + lcs(pat1, pat2, plen1-1, plen2-1, True)
        else:
            return 0
    res = 0
    if pat1[plen1-1] == pat2[plen2-1]:
        res = 1 + lcs(pat1, pat2, plen1-1, plen2-1, True)
    return max(res, max(lcs(pat1, pat2, plen1-1, plen2, False), lcs(pat1, pat2, plen1, plen2-1, False)))

if __name__ == '__main__':
    pat1 = "ABCDEF"
    pat2 = "ZCDEMF"
    print "LCS Substring length: ", lcs(pat1, pat2, len(pat1), len(pat2), False)

