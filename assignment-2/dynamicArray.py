class DynamicArray:
    def __init__(self):
        self.size = 0        
        self.capacity = 1    
        self.array = [None] * self.capacity

    def append(self, value):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        
        self.array[self.size] = value
        self.size += 1
        print(f"Append {value}: Size={self.size}, Capacity={self.capacity}")

    def _resize(self, new_capacity):
        print(f"--- Resizing: {self.capacity} -> {new_capacity} ---")
        new_arr = [None] * new_capacity
        for i in range(self.size):
            new_arr[i] = self.array[i]
        self.array = new_arr
        self.capacity = new_capacity

    def pop(self):
        if self.size > 0:
            val = self.array[self.size - 1]
            self.array[self.size - 1] = None
            self.size -= 1
            print(f"Popped: Size={self.size}, Capacity={self.capacity}")
            return val


da = DynamicArray()
for i in range(1, 6):
    da.append(i * 10)
da.pop()