# http://www.geeksforgeeks.org/searching-for-patterns-set-2-kmp-algorithm/
# KMP algorithm for fast pattern matching in text
# O(n)

def LPS(pattern):

    plength = len(pattern)
    lps = [0] * plength

    j = 0
    i = 1

    while i < plength:
        if pattern[j] == pattern[i]:
            lps[i] = j + 1
            j += 1
            i += 1
        elif j != 0:
            j = lps[j-1]
        else:
            lps[i] = 0
            i += 1
    return lps

def kmp_search(pattern, text):
    plength = len(pattern)
    tlength = len(text)
    
    lps = LPS(pattern)

    i = 0
    j = 0
    while i < tlength:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == plength:
            print "Pattern Found: @Index => ", i-j
            j = lps[j-1]
        elif i < tlength and pattern[j] != text[i]:
            # Tricky case
            if j != 0:
                j = lps[j-1]
            else:
                i += 1


if __name__ == '__main__':

    params = [
            ("ABABCABAB", "ABABDABACDABABCABAB"),
            ('AAAAB', 'AAAAAAAAAAAAAAAAAB'),
            ('ABABAC', 'ABABABCABABABCABABABAC')]

    for pattern, text in params:
        kmp_search(pattern, text)
