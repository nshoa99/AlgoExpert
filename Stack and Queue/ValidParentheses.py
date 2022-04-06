# https://leetcode.com/problems/valid-parentheses/
# O(n) Time and Space complexity
def isValid(s):
    stack = []
    mapping = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    for character in s:
        if character not in mapping:
            stack.append(character)
        else:
            if len(stack) > 0 and stack[-1] == mapping[character]:
                stack.pop()
            else:
                return False

    return len(stack) == 0
