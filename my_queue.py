import queue

# Create a new queue
my_queue = queue.Queue()

# Enqueue (add) elements to the queue
my_queue.put(10)
my_queue.put(20)
my_queue.put(30)

# Dequeue (remove and return) elements from the queue
element = my_queue.get()
print("Dequeued element:", element)

# Check if the queue is empty
is_empty = my_queue.empty()
print("Is the queue empty?", is_empty)

# Get the size of the queue
queue_size = my_queue.qsize()
print("Queue size:", queue_size)

# Peek at the front element (without removing it)
front_element = my_queue.queue[0]

print("Front element:", front_element)

#Proprity queue

# import queue

# # Create a priority queue
# my_priority_queue = queue.PriorityQueue()

# # Enqueue items with associated priorities
# my_priority_queue.put((5, "Item 5"))
# my_priority_queue.put((1, "Item 1"))
# my_priority_queue.put((3, "Item 3"))
# my_priority_queue.put((2, "Item 2"))
# my_priority_queue.put((4, "Item 4"))

# # Dequeue items (higher priority items are dequeued first)
# while not my_priority_queue.empty():
#     priority, item = my_priority_queue.get()
#     print(f"Dequeued item: {item} with priority {priority}")

