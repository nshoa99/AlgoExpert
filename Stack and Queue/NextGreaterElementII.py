# https://www.algoexpert.io/questions/Next%20Greater%20Element
# Time complexity O(n) | Space complexity O(n)

def nextGreaterElement(array):
    result = [-1] * len(array)
    stack = []
    stackIndices = []
    for _ in range(2):
        i = 0
        while i < len(array):
            if len(stack) == 0 or array[i] <= stack[-1]:
                stack.append(array[i])
                stackIndices.append(i)
                i += 1
            else:
                result[stackIndices[-1]] = array[i]
                stack.pop()
                stackIndices.pop()

    return result


print(nextGreaterElement([2, 5, -3, -4, 6, 7, 2]))
# Expected Output: [5, 6, 6, 6, 7, -1, 5]
