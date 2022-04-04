# https://www.algoexpert.io/questions/Spiral%20Traverse
# O(n) time | O(n) space
def spiralTraverse(array):
    result = []

    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1

    while startCol <= endCol and startRow <= endRow:
        for col in range(startCol, endCol + 1):
            result.append(array[startRow][col])

        for row in range(startRow + 1, endRow + 1):
            result.append(array[row][endCol])

        for col in reversed(range(startCol, endCol)):
          if startRow == endRow:
            break
          result.append(array[endRow][col])

        for row in reversed(range(startRow + 1, endRow)):
          if startCol == endCol:
            break
          result.append(array[row][startCol])

        startCol += 1
        endCol -= 1
        startRow += 1
        endRow -= 1
    return result

print(spiralTraverse([
    [1, 2, 3, 4],
    [10, 11, 12, 5],
    [9, 8, 7, 6]
  ]))

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 11]
