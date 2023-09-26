# Algorithm:

# 1.If the input array has length 0 or 1, return the array as it is already sorted.
# 2.Choose the first element of the array as the pivot element.
# 3.Create two empty lists, left and right.
# 4.For each element in the array except for the pivot:
# a. If the element is smaller than the pivot, add it to the left list.
# b. If the element is greater than or equal to the pivot, add it to the right list.
# 5.Recursively call quicksort on the left and right lists.
# 6.Concatenate the sorted left list, the pivot element, and the sorted right list.
# 7.Return the concatenated list.

# Approach 2: Quicksort using list comprehension

def quicksort(arr):
	if len(arr) <= 1:
		return arr
	else:
		pivot = arr[0]
		left = [x for x in arr[1:] if x < pivot]
		right = [x for x in arr[1:] if x >= pivot]
		return quicksort(left) + [pivot] + quicksort(right)

# Example usage
arr = [1, 7, 4, 1, 10, 9, -2]
sorted_arr = quicksort(arr)
print("Sorted Array in Ascending Order:")
print(sorted_arr)
