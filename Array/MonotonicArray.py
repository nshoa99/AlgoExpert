#https://www.algoexpert.io/questions/Monotonic%20Array
#Time complexity O(n), Space complexity O(1)
def isMonotonic(array):
    isNonDecreasing = True
    isNonIncreasing = True
    for i in range(1, len(array)): 
        if array[i] > array[i - 1]:
            isNonIncreasing = False
        if array[i] < array[i - 1]:
            isNonDecreasing = False

    return isNonDecreasing or isNonIncreasing 
# True(False) or True (False) = True
# False or False = False
print(isMonotonic([1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 11]))