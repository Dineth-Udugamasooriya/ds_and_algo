class DynamicArray:
    def __init__(self):
        self.array = []

    def append(self, value):
        self.array.append(value)

    def insert(self, index, value):
        self.array.insert(index, value)

    def remove(self, value):
        self.array.remove(value)

    def display(self):
        print(self.array)

# Example usage:
if __name__ == "__main__":
    my_dynamic_array = DynamicArray()
    my_dynamic_array.append(10)
    my_dynamic_array.append(20)
    my_dynamic_array.append(30)
    my_dynamic_array.display()  # Output: [10, 20, 30]

    my_dynamic_array.insert(1, 15)
    my_dynamic_array.display()  # Output: [10, 15, 20, 30]

    my_dynamic_array.remove(20)
    my_dynamic_array.display()  # Output: [10, 15, 30]

# In this example:

# We define a DynamicArray class that wraps a Python list.
# The append method appends a value to the end of the dynamic array.
# The insert method inserts a value at a specific index.
# The remove method removes the first occurrence of a value from the dynamic array.
# The display method prints the contents of the dynamic array.
# The example usage section demonstrates these operations on a dynamic array-like data structure implemented