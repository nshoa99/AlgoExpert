# https://www.algoexpert.io/questions/Generate%20Document

def generateDocument(characters, document):
    counting_characters = {}
    counting_document = {}

    for c in characters:
        if c in counting_characters:
            counting_characters[c] += 1
        else:
            counting_characters[c] = 1

    for c in document:
        if c in counting_document:
            counting_document[c] += 1
        else:
            counting_document[c] = 1

    for c in document:
        if c not in counting_characters or counting_characters[c] < counting_document[c]:
            return False

    return True


print(generateDocument("A", "a"))
