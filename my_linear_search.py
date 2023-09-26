def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index  # Return the index where the target element is found
    return -1  # Return -1 if the target element is not in the list

# Example usage:
my_list = [10, 20, 30, 40, 50, 60]
target_element = 40

# numbers = []

# for i in range(10000001):
#     numbers.append(i)

# # Now, the 'numbers' list contains the numbers from 0 to 100,000

# target_element = 7777777

result = linear_search(my_list, target_element)

if result != -1:
    print(f"Element {target_element} found at index {result}")
else:
    print(f"Element {target_element} not found in the list")
