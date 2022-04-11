# https://www.algoexpert.io/questions/Longest%20Palindromic%20Substring
# Time complexity O(n^2) | Space complexity O(n)

def longestPalindromicSubstring(string):
    logest = ""
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i: j + 1]
            if isPalindrome(substring) and len(substring) > len(logest):
                logest = substring

    return logest


def isPalindrome(string):
    i, j = 0, len(string) - 1
    while i < j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True


print(longestPalindromicSubstring("abaxyzzyxf"))
