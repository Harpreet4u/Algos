# Longest palindrome substring
# O(n^2) Easy while loop solution

def longest_palindrome(arr):

    longest_substring = 1
    for i in xrange(len(arr)):

        palindrome = 0
        x = i
        y = i+1
        while x >=0 and y< len(arr) and arr[x] == arr[y]:
            x-=1
            y+=1
            palindrome += 2

        longest_substring = max(longest_substring, palindrome)

        palindrome = 1
        x = i-1
        y = i+1
        while x>=0 and y<len(arr) and arr[x] == arr[y]:
            x-=1
            y+=1
            palindrome += 2
        longest_substring = max(longest_substring, palindrome)

    return longest_substring

if __name__ == '__main__':
    print longest_palindrome("abba")
    print longest_palindrome("abbababba")
    print longest_palindrome("babcbaabcbaccba")
