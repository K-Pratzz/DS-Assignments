class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x): 
        """Adds an element to the rear of the queue in O(1)."""
        new_node = Node(x)
        
        if self.tail is None:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        """Removes the front element and handles underflow safely."""
        if self.is_empty():
            print("Queue Underflow: Cannot dequeue from an empty queue.")
            return None
        
        removed_data = self.head.data
        self.head = self.head.next
        
        if self.head is None:
            self.tail = None
            
        return removed_data

    def get_front(self):
        """Returns the front element without removing it."""
        if self.is_empty():
            return "Queue is Empty"
        return self.head.data

    def is_empty(self):
        return self.head is None

    def display(self):
        elements = []
        curr = self.head
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        print("Front -> " + " -> ".join(elements) + " <- Rear" if elements else "Queue is Empty")


q = Queue()

print("Operations Sequence:")
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()

print(f"Front element: {q.get_front()}")

print(f"Removed: {q.dequeue()}")
q.display()

print(f"Removed: {q.dequeue()}")
q.display()

print(f"Final State (is empty?): {q.is_empty()}")