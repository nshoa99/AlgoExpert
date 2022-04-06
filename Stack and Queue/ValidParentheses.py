# https://leetcode.com/problems/valid-parentheses/
# O(n) Time and Space complexity
def isValid(s):
    stack = []
    for character in s:
        if character == '(':
            stack.append(character)
        else:
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                return False

    return len(stack) == 0
