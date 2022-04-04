# https://www.algoexpert.io/questions/Move%20Element%20To%20End
# Time complexity O(n), Space complexity O(1)
def moveElementToEnd(array, toMove):
    i, j = 0, len(array) - 1
    while i < j:
        if array[i] == toMove and array[j] != toMove:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
        if array[i] != toMove:
            i += 1
        if array[j] == toMove:
            j -= 1

    return array


print(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2))
