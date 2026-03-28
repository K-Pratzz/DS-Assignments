class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x):  #enquqe adds ele to the last
        new_node = Node(x)
        
        if self.tail is None:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self): #removes from end 
        if self.is_empty(): #empty queue
            print("Queue Underflow.")
            return None
        
        removed_data = self.head.data
        self.head = self.head.next
        
        if self.head is None:
            self.tail = None
            
        return removed_data

    def get_front(self): #top element of queue
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
        print(elements)


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

print(f"is empty?: {q.is_empty()}")