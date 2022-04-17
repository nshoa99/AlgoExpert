# https://www.algoexpert.io/questions/Bubble%20Sort
# Average: Time complexity O(n^2) | Space complexity O(1)

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array


print(bubbleSort([8, 5, 2, 9, 5, 6, 3]))
