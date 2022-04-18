# https://www.algoexpert.io/questions/Selection%20Sort
# Time complexity O(n^2) | Space complexity O(1)

def selectionSort(array):
    for i in range(len(array)):
        smallest_idx = i
        for j in range(i, len(array)):
            if array[j] < array[smallest_idx]:
                smallest_idx = j
        if i != smallest_idx:
            array[i], array[smallest_idx] = array[smallest_idx], array[i]
    return array


print(selectionSort([8, 5, 2, 9, 5, 6, 3]))
