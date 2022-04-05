# https://www.algoexpert.io/questions/Class%20Photos
# O(nlogn) Time | O(1) space complexity
def classPhotos(redShirtHeights, blueShirtHeights):
    for i in range(len(redShirtHeights)):
        if sum(redShirtHeights) > sum(blueShirtHeights):
            if redShirtHeights[i] <= blueShirtHeights[i]:
                return False
        else:
            if blueShirtHeights[i] <= redShirtHeights[i]:
                return False
    return True


print(classPhotos([5, 8, 1, 3, 4], [6, 9, 2, 4, 5]))