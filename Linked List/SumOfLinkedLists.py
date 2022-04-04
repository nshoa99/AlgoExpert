class LinkedList:
    def __init__(self, value):
        self.value
        self.next = None

# O(max(m, n)) time | O(max(m, n)) space


def sumOfLinkedList(linkedListOne, linkedListTwo):
    newLinkedListHeadPointer = LinkedList(0)
    currentNode = newLinkedListHeadPointer
    carry = 0

    nodeOne = linkedListOne
    nodeTwo = linkedListTwo
    while nodeOne or nodeTwo or carry != 0:
        valueOne = nodeOne.value if nodeOne else 0
        valueTwo = nodeTwo.value if nodeTwo else 0
        sumOfValue = valueOne + valueTwo + carry
        newValue = sumOfValue % 10
        carry = sumOfValue // 10
        newNode = LinkedList(newValue)
        currentNode.next = newNode
        currentNode = newNode

        nodeOne = nodeOne.next if nodeOne else None
        nodeTwo = nodeTwo.next if nodeTwo else None

    return newLinkedListHeadPointer.next
