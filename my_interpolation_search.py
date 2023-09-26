# Python3 program to implement
# interpolation search
# with recursion

# If x is present in arr[0..n-1], then
# returns index of it, else returns -1.


def interpolationSearch(arr, lo, hi, x):

	# Since array is sorted, an element present
	# in array must be in range defined by corner
	if (lo <= hi and x >= arr[lo] and x <= arr[hi]):

		# Probing the position with keeping
		# uniform distribution in mind.
		pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) *
					(x - arr[lo]))

		# Condition of target found
		if arr[pos] == x:
			return pos

		# If x is larger, x is in right subarray
		if arr[pos] < x:
			return interpolationSearch(arr, pos + 1,
									hi, x)

		# If x is smaller, x is in left subarray
		if arr[pos] > x:
			return interpolationSearch(arr, lo,
									pos - 1, x)
	return -1

# Driver code


# Array of items in which
# search will be conducted
arr = [10, 12, 13, 16, 18, 19, 20,
	21, 22, 23, 24, 33, 35, 42, 47]
n = len(arr)

# Element to be searched
x = 18
index = interpolationSearch(arr, 0, n - 1, x)

if index != -1:
	print("Element found at index", index)
else:
	print("Element not found")

# This code is contributed by Hardik Jain


############# Second Methos

# def interpolation_search(arr, target):
#     left, right = 0, len(arr) - 1

#     while left <= right and arr[left] <= target <= arr[right]:
#         # Calculate the position using interpolation formula
#         pos = left + ((target - arr[left]) * (right - left)) // (arr[right] - arr[left])

#         if arr[pos] == target:
#             return pos  # Target element found at position 'pos'

#         if arr[pos] < target:
#             left = pos + 1  # Adjust the left boundary
#         else:
#             right = pos - 1  # Adjust the right boundary

#     return -1  # Target element not found

# # Example usage:
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# target_element = 60

# result = interpolation_search(my_list, target_element)

# if result != -1:
#     print(f"Element {target_element} found at index {result}")
# else:
#     print(f"Element {target_element} not found in the list")
