# https://www.algoexpert.io/questions/Quick%20Sort
# Time complexity O(nlogn) | Space complexity O(logn)

# Best sort performance


def quickSort(array):
    quickSortHelper(array, 0, len(array) - 1)
    return array

# Recursion


def quickSortHelper(array, startIdx, endIdx):

    # base case
    if startIdx >= endIdx:
        return
    pivotIdx = startIdx
    leftIdx = startIdx + 1
    rightIdx = endIdx
    while rightIdx >= leftIdx:
        if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
            array[leftIdx], array[rightIdx] = array[rightIdx], array[leftIdx]
        if array[leftIdx] <= array[pivotIdx]:
            leftIdx += 1
        if array[rightIdx] >= array[pivotIdx]:
            rightIdx -= 1
    array[pivotIdx], array[rightIdx] = array[rightIdx], array[pivotIdx]
    leftSubarrayIsSmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx + 1)
    if leftSubarrayIsSmaller:
        quickSortHelper(array, startIdx, rightIdx - 1)
        quickSortHelper(array, rightIdx + 1, endIdx)
    else:
        quickSortHelper(array, rightIdx + 1, endIdx)
        quickSortHelper(array, startIdx, rightIdx - 1)
