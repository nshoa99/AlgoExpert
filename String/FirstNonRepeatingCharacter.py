# https://www.algoexpert.io/questions/First%20Non-Repeating%20Character
# Time complexity O(n) | Space complexity O(n)


def firstNonRepeatingCharacter(string):
    counting = {}
    for c in string:
        if c in counting:
            counting[c] += 1
        else:
            counting[c] = 1
    
    for idx, c in enumerate(string):
        if counting[c] == 1:
            return idx
    return -1

print(firstNonRepeatingCharacter("abcdcaf"))
