class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def insert_after(self, prev_data, new_data):
        new_node = Node(new_data)
        current = self.head
        while current:
            if current.data == prev_data:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

# Example usage:
if __name__ == "__main__":
    my_linked_list = LinkedList()
    my_linked_list.append(10)
    my_linked_list.append(20)
    my_linked_list.append(30)
    my_linked_list.prepend(5)
    my_linked_list.display()  # Output: 5 -> 10 -> 20 -> 30
    my_linked_list.delete(20)
    my_linked_list.display()  # Output: 5 -> 10 -> 30
    my_linked_list.insert_after(10, 15)
    my_linked_list.display()  # Output: 5 -> 10 -> 15 -> 30
