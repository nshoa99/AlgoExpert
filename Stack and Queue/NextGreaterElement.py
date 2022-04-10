# Leetcode: https://leetcode.com/problems/next-greater-element-i/
# Time complexity O(n) | Extra space complexity O(n)

def nextGreaterElement(nums1, nums2):
    result = [-1] * len(nums1)
    mapping = {nums1[i]: i for i in range(len(nums1))}
    stack = []
    i = 0
    while i < len(nums2):
        if len(stack) == 0 or nums2[i] < stack[-1]:
            stack.append(nums2[i])
            i += 1
        else:
            if stack[-1] in mapping:
                result[mapping[stack[-1]]] = nums2[i]
            stack.pop()
    return result

print(nextGreaterElement([2, 5, -3, -4, 6, 7], [2, 5, -3, -4, 6, 7, 8]))