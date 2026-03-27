class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_after_node(self, target_data, x):
        temp = self.head
        while temp and temp.data != target_data:
            temp = temp.next
        
        if not temp:
            print(f"Target {target_data} not found.")
            return

        new_node = Node(x)
        new_node.next = temp.next
        new_node.prev = temp
        
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node
        self.display()

    def delete_at_position(self, pos):
        if not self.head: return
        
        temp = self.head
        if pos == 0:
            self.head = temp.next
            if self.head: self.head.prev = None
        else:
            for _ in range(pos):
                if temp is None: break
                temp = temp.next
            
            if not temp:
                print("Position out of bounds.")
                return
            
            if temp.next:
                temp.next.prev = temp.prev
            if temp.prev:
                temp.prev.next = temp.next
        
        self.display()

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next: last = last.next
        last.next = new_node
        new_node.prev = last

    def display(self):
        elems = []
        curr = self.head
        while curr:
            elems.append(str(curr.data))
            curr = curr.next
        print(" <-> ".join(elems) if elems else "Empty List")


dll = DoublyLinkedList()
for i in [10, 20, 30]: dll.append(i)
print("Initial List:")
dll.display()
print("\nInsert 25 after 20:")
dll.insert_after_node(20, 25)
print("\nDelete at position 2 (0-indexed):")
dll.delete_at_position(2)