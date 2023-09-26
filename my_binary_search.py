import time

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Calculate the middle index

        if arr[mid] == target:
            return mid  # Target element found, return its index
        elif arr[mid] < target:
            left = mid + 1  # Adjust the left boundary
        else:
            right = mid - 1  # Adjust the right boundary

    return -1  # Target element not found

# Example usage:


# Create an empty list to store the numbers
numbers = []

# Use a for loop to generate numbers from 0 to 100,000
for i in range(10000001):
    numbers.append(i)

# Now, the 'numbers' list contains the numbers from 0 to 100,000

target_element = 7777777

# Record the start time
start_time = time.time()


result = binary_search(numbers, target_element)

# Record the end time
end_time = time.time()

if result != -1:
    print(f"Element {target_element} found at index {result}")
else:
    print(f"Element {target_element} not found in the list")

elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")
