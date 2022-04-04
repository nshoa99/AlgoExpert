# https://www.algoexpert.io/questions/First%20Duplicate%20Value
# Solution 1: Time complexity O(n^2) , Space complexity O(1)

# def firstDuplicateValue(array):
#     minIndex = len(array)
#     for i in range(0, len(array) - 1):
#         for j in range(i + 1, len(array)):
#             if array[i] == array[j]:
#                 if j < minIndex:
#                     minIndex = j
#     if minIndex >= len(array):
#         return -1
#     else:
#         return array[minIndex]


# Solution 2: Time complexity O(n), Space complexity O(n)
# def firstDuplicateValue(array):
#     seen = []
#     for i in range(len(array)):
#         if array[i] in seen:
#             return array[i]
#         seen.append(array[i])
#     return -1


# Solution 3: Time complexity O(n), Space complexity O(1)
def firstDuplicateValue(array):
    for i in range(len(array)):
        value = abs(array[i]) - 1
        if array[value] < 0:
            return abs(array[i])
        array[value] *= -1
    return -1

print(firstDuplicateValue([1, 1]))  # Output: 1
