# https://www.algoexpert.io/questions/Task%20Assignment
# O(nlogn) Time | O(n) Space complexity

def taskAssignment(k, tasks):
    result = []
    sorted_tasks = sorted(tasks)
    taskDurationToIndices = {}
    for idx, taskDuration in enumerate(tasks):
        if taskDuration in taskDurationToIndices:
            taskDurationToIndices[taskDuration].append(idx)
        else:
            taskDurationToIndices[taskDuration] = [idx]

    i, j = 0, len(tasks) - 1
    while i < j:
        result.append([
            taskDurationToIndices[sorted_tasks[i]][-1],
            taskDurationToIndices[sorted_tasks[j]][-1],
        ])

        taskDurationToIndices[sorted_tasks[i]].pop()
        taskDurationToIndices[sorted_tasks[j]].pop()
        i += 1
        j -= 1

    return result


print(taskAssignment(3, [1, 3, 5, 3, 1, 4]))
