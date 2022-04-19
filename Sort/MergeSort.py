# https://www.algoexpert.io/questions/Merge%20Sort
# Time complexity O(nlogn) | Space complexity O(n)


def mergeSort(array):
    sortedArray = divide(0, len(array) - 1, array)
    return sortedArray

# Recursion
def divide(i, j, array): #O(logn)
	middle = (i + j) // 2
	
	if i == j:
		return [array[i]]
	
	array1 = divide(i, middle, array)
	array2 = divide(middle + 1, j, array)
	
	return merge(array1, array2)

# Using two pointers 
def merge(array1, array2): #O(n)
	i, j = 0, 0 
	new_array = []
	
	while i < len(array1) and j < len(array2):
		if array1[i] < array2[j]:
			new_array.append(array1[i])
			i += 1
		else:
			new_array.append(array2[j])
			j += 1
	
	if i < len(array1):
		new_array += array1[i:]
	if j < len(array2):
		new_array += array2[j:]
	
	return new_array
	
