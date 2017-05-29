# Preprocessing step of KMP algorithm
# Finding longest proper prefix which is also a suffix
# O (n) 

def LPS(pattern):
    plength = len(pattern)
    lps = [0] * plength

    # comparision pointers
    i = 1
    j = 0 # start is always zero

    while i < plength:
        if pattern[i] == pattern[j]:
            lps[i] = j + 1
            j += 1
            i += 1
        elif j != 0:
            j = lps[j-1]
        else:
            j = 0
            i += 1

    return lps


if __name__ == '__main__':
    print LPS("ABABCABAB")
    
    patterns = ["AAAA", "ABCDE", "AABAACAABAA", "AAACAAAAAC", "AAABAAA"]
    results = [
            [0,1,2,3],
            [0,0,0,0,0],
            [0,1,0,1,2,0,1,2,3,4,5],
            [0,1,2,0,1,2,3,3,3,4],
            [0,1,2,0,1,2,3]
            ]

    for pattern, result in zip(patterns, results):
        res = LPS(pattern)
        print res
        assert res == result

    
