# https://www.algoexpert.io/questions/Sunset%20Views
# Time complexity O(n) | Space complexity O(n)

def sunsetViews(buildings, direction):
    stack = []
    stackIdx = []

    if direction == 'EAST':
        buildings.append(0)
        for i in range(0, len(buildings) - 1):
            if buildings[i] > buildings[i + 1]:
                # if len(stack) == 0 or buildings[i] < stack[-1]:
                #     stack.append(buildings[i])
                #     stackIdx.append(i)
                # else:
                while len(stack) > 0 and buildings[i] >= stack[-1]:
                    stack.pop()
                    stackIdx.pop()
                stack.append(buildings[i])
                stackIdx.append(i)
    else:
        if buildings:
            buildings.append(0)
            stack.append(buildings[0])
            stackIdx.append(0)
            for i in range(1, len(buildings) - 1):
                if buildings[i] > buildings[i - 1] and buildings[i] > stack[-1]:
                    stack.append(buildings[i])
                    stackIdx.append(i)
        else:
            return []
    return stackIdx


print(sunsetViews([2, 4], 'WEST'))
