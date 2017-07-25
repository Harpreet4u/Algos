# Longest palindrome substring
# O(n) --> Manacher's algorithms

"""
Manacher's condition:
    Case 1 : Right side palindrome is totally contained under current palindrome. In this case do not consider this as center.
    Case 2 : Current palindrome is proper suffix of input. Terminate the loop in this case. No better palindrom will be found on right.
    Case 3 : Right side palindrome is proper suffix and its corresponding left side palindrome is proper prefix of current palindrome. Make largest such point as next center.
    Case 4 : Right side palindrome is proper suffix but its left corresponding palindrome is be beyond current palindrome. Do not consider this as center because it will not extend at all.

"""

def longest_palindrome_manachers(input_string):
    
    new_input = ""
    index = 0
    # pre-processing for even length palindromes as algo works on odd lengths
    for i in xrange(2*len(input_string)+1):
        if i%2 != 0:
            new_input += input_string[index]
            index+=1
        else:
            new_input += '$'

    T = [0]*(len(new_input))
    i = 0
    start = end = 0
    while i < len(new_input):
        while start > 0 and end < (len(new_input)-1) and new_input[start-1] == new_input[end+1]:
            start -= 1
            end += 1

        T[i] = end - start + 1

        if end == (len(new_input) - 1):
            break

        new_center = end + (1 if i%2 == 0 else 0)
        
        for j in xrange(i+1, end+1):
            T[j] = min(T[i-(j-i)], 2*(end-j)+1)
            if j + T[i-(j-i)]/2 == end:
                new_center = j
                break

        i = new_center
        start = i - T[i]/2
        end = i + T[i]/2

    maxx = 0
    for i in T:
        if i/2 > maxx:
            maxx = i/2

    return maxx


if __name__ == '__main__':
    assert longest_palindrome_manachers("abba") == 4
    assert longest_palindrome_manachers("abbababba") == 9
    assert longest_palindrome_manachers("babcbaabcbaccba") == 10
