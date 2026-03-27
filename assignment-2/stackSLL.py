class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = SLLNode(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty(): return None
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        return self.top.data if self.top else None

    def is_empty(self):
        return self.top is None

def is_balanced(expression):
    stack = Stack()
    mapping = {')': '(', '}': '{', ']': '['}
    
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