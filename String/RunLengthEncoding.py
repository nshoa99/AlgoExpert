# https://www.algoexpert.io/questions/Run-Length%20Encoding
# Time complexity O(n) | Space complexity O(n)


def runLengthEncoding(string):
    encodedChars = []
    length = 1
    for i in range(1, len(string)):
        currentCharacter = string[i]
        previousCharacter = string[i - 1]

        if currentCharacter != previousCharacter or length == 9:
            encodedChars.append(str(length))
            encodedChars.append(previousCharacter)
            length = 0
        length += 1
    encodedChars.append(str(length))
    encodedChars.append(string[-1])

    return "".join(encodedChars)


print(runLengthEncoding("aaaaaaaaaaaaaabvc"))
