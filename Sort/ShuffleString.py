# https://leetcode.com/problems/shuffle-string/
# Time complexity (n) | Space complexity O(n)

def restoreString(s, indices):
    mapping = {indices[i]: s[i] for i in range(len(indices))}
    indices.sort()
    result = []

    for i in range(len(indices)):
        result.append(mapping[indices[i]])

    return "".join(result)


print(restoreString(s="codeleet", indices=[4, 5, 6, 7, 0, 2, 1, 3]))

# Expected output: leetcode