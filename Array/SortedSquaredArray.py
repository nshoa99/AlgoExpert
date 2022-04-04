# https://www.algoexpert.io/questions/Sorted%20Squared%20Array

#S1 Time complexity O(n), Space complexity O(1)
def sortedSquaredArray(array):
    squaredArray = [0] * len(array)
    i, j = 0, len(array) - 1
    k = 0
    while i <= j:

        if abs(array[j]) > abs(array[i]):
            squaredArray[len(array) - k - 1] = array[j]*array[j]
            j -= 1
            k += 1
        else:
            squaredArray[len(array) - k - 1] = array[i]*array[i]
            k += 1
            i += 1

    return squaredArray


print(sortedSquaredArray([1, 2, 3, 4, 5]))
