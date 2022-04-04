# https://www.algoexpert.io/questions/Three%20Number%20Sum
# Time complexity O(n^2), Space complexity O(n)


def threeNumberSum(array, targetSum):
    results = []
    array.sort()
    for k in range(len(array) - 2):
        currentPosition = k
        leftPointer, rightPointer = currentPosition + 1, len(array) - 1
        while leftPointer < rightPointer:
            if array[currentPosition] + array[leftPointer] + array[rightPointer] == targetSum:
                results.append(
                    [array[currentPosition], array[leftPointer], array[rightPointer]])
                leftPointer += 1
                rightPointer -= 1
            elif array[currentPosition] + array[leftPointer] + array[rightPointer] < targetSum:
                leftPointer += 1
            else:
                rightPointer -= 1

    return results


print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))
