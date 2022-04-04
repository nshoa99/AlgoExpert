# https://www.algoexpert.io/questions/Validate%20Subsequence

# #S1 Time complexity O(n), Space complexity O(1)
# def isValidSubsequence(array, sequence):
#     j = 0
#     for num in array:
#         if num == sequence[j] and j < len(sequence):
#             j += 1

#         if j == len(sequence):
#             return True

#     return False

# print(isValidSubsequence([1, 1, 1, 1, 1], [1, 1, 1]))

# S2 (while loop ) Time complexity O(n), Space complexity O(1)

def isValidSubsequence(array, sequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)

print(isValidSubsequence([1, 1, 1, 1, 1], [1, 1, 1]))

