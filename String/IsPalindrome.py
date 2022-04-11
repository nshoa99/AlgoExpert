# https://www.algoexpert.io/questions/Palindrome%20Check
# Time complexity O(n) | Space complexity O(1)
 
def isPalindrome(string):
    i, j = 0, len(string) - 1
    while i < j:
        if string[i] != string[j]:
            return False
        i += 1
        j -=1
    return True