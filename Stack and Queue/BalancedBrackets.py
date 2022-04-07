# https://www.algoexpert.io/questions/Balanced%20Brackets
# Time complexity O(n) | Extra space complexity O(n)

def balancedBrackets(string):
    stack = []
    mapping = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    openingBrackets = "[({"
    closingBrackets = ")}]"
    for c in string:
        if c in openingBrackets:
            stack.append(c)
        elif c in closingBrackets:
            if len(stack) > 0 and stack[-1] == mapping[c]:
                stack.pop()
            else:
                return False
    return len(stack) == 0


print(balancedBrackets("{}gawgw()"))
