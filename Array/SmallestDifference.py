#https://www.algoexpert.io/questions/Smallest%20Difference
# Time complexity O(nlog(n) + mlog(m)), Space complexity O(1)
def smallestDifference(arrayOne, arrayTwo):
    result = []
    i, j = 0, 0
    arrayOne.sort()
    arrayTwo.sort()
    smallestDiff = abs(arrayOne[0] - arrayTwo[0])

    while i < len(arrayOne) and j < len(arrayTwo):
        if abs(arrayOne[i] - arrayTwo[j]) == 0:
            return [arrayOne[i], arrayTwo[j]]
        different = abs(arrayOne[i] - arrayTwo[j])
        if different < smallestDiff:
            smallestDiff = different
            result.append(arrayOne[i])
            result.append(arrayTwo[j])
        if arrayOne[i] < arrayTwo[j]:
            i += 1
        else:
            j += 1
    
    return result[-2:]

print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))