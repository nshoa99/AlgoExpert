# https://www.algoexpert.io/questions/Three%20Number%20Sort
# Time complexity O(n) | Space complexity O(1)


def threeNumberSort(array, order):
    leftIdx = 0
    for orderIdx in range(len(order) - 1):
        rightIdx = len(array) - 1
        while leftIdx < rightIdx:
            if array[leftIdx] == order[orderIdx]:
                leftIdx += 1
            if array[leftIdx] != order[orderIdx] and array[rightIdx] == order[orderIdx]:
                array[leftIdx], array[rightIdx] = array[rightIdx], array[leftIdx]
                leftIdx += 1
            rightIdx -= 1
    return array


print(threeNumberSort([1, 0, 0, -1, -1, 0, 1, 1], [0, 1, -1]))
