# https://www.algoexpert.io/questions/Tandem%20Bicycle
# O(nlogn) Time | O(1) Space complexity

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    result = 0
    for i in range(len(redShirtSpeeds)):
        if fastest:
            redShirtSpeeds.sort()
            blueShirtSpeeds.sort(reverse=True)
            result += max(redShirtSpeeds[i], blueShirtSpeeds[i])
        else:
            redShirtSpeeds.sort()
            blueShirtSpeeds.sort()
            result += max(redShirtSpeeds[i], blueShirtSpeeds[i])

    return result


print(tandemBicycle([5, 5, 3, 9, 2], [3, 6, 7, 2, 1], False))
