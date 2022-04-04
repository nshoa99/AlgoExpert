# 
# O(n) time | O(n) space

def longestPeak(array):
    longestPeak = 0 
    i = 1
    while i < len(array) - 1:
        if array[i - 1] < array[i] and array[i] > array[i + 1]:
            leftInd, rightIdx = i - 1, i + 1
            while leftInd >= 0 and array[leftInd - 1] <= array[leftInd]:
                leftInd -= 1
            
            while rightIdx <= len(array) - 1 and array[rightIdx + 1] <= array[rightIdx]:
                rightIdx +=1

            if rightIdx - leftInd + 1 > longestPeak:
                longestPeak = rightIdx - leftInd + 1
                i = rightIdx
        else: 
            i += 1

    return longestPeak

print(longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
))
        