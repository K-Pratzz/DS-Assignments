class SLLNode:
    def __init__(self, data):
        self.data = data #will contain the data
        self.next = None#next adrress node

class Stack:
    def __init__(self):
        self.top = None #head id=s none at beginning

    def push(self, data):
        new_node = SLLNode(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty(): return None
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self): #show top ele if not empty
        return self.top.data if self.top else None

    def is_empty(self): #check if stack is empty
        return self.top is None

def is_balanced(expression):
    stack = Stack()
    mapping = {')': '(', '}': '{', ']': '['} #inside stack goes ( after that till ) goes everthing pops back 
    
    for char in expression:
        if char in mapping.values():
            stack.push(char)
        elif char in mapping.keys(): 
            if stack.is_empty() or stack.pop() != mapping[char]:
                return False
    return stack.is_empty()


test_strings = ["([]){}", "([)]", "((()))", "(()]"]
for s in test_strings:
    print(f"String: {s:8} -> Balanced: {is_balanced(s)}")