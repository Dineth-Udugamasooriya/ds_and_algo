class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

# Create a new stack
my_stack = Stack()

# Push (add) elements to the stack
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

# Element to search for
element_to_search = 20

found = False

# Search for the element in the stack
while not my_stack.is_empty():
    top_element = my_stack.pop()
    if top_element == element_to_search:
        found = True
        break

if found:
    print(f"{element_to_search} found in the stack.")
else:
    print(f"{element_to_search} not found in the stack.")
