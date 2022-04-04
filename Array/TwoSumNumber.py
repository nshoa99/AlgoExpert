#https://www.algoexpert.io/questions/Two%20Number%20Sum
# My dummy code
# def twoNumberSum(array, targetSum):
#     result = []
#     for i in range(len(array)):
#         for j in range(len(array)):
#             if array[i] + array[j] == targetSum and i != j:
#                 result.append(array[i])
#                 result.append(array[j])
#                 break

#         if len(result) == 2 and sum(result) == targetSum:
#             break
#     if sum(result) == targetSum and len(result) == 2:
#         return result
#     else:
#         return []

### Solution 1:

# def twoNumberSum(array, targetSum):
#     for i in range(len(array) - 1):
#         for j in range(i + 1, len(array)):
#             if array[i] + array[j] == targetSum:
#                 return [array[i], array[j]]
#     return []

# Time complexity O(n^2) | Space complexity O(1)

### Solution 2:
def twoNumberSum(array, targetSum):
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in array and potentialMatch != num:
            return [num, potentialMatch]

    return []

# O(1) ST


### Solution 3: Hash Table
print(twoNumberSum([4, 6, 1], 5))