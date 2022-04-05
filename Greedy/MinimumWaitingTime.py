def minimumWaitingTime(queries):
    queries.sort()
    sum = 0 
    minimumTime = 0
    for i in range(1, len(queries)):
        sum += queries[i - 1]
        minimumTime += sum 
    return minimumTime

# O(nlogn) Time | O(1) Space complexity


print(minimumWaitingTime([3, 2, 1, 2, 6]))
