# Leetcode: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
# Time complexity O(n), Extra space complexity O(n)

def removeDuplicates(s):
    stack = []
    for c in s:
        if len(stack) == 0 or c != stack[-1]:
            stack.append(c)
        else:
            stack.pop()
    return "".join(stack)