# Binary Search Tree
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)
    
    def _insert(self, root, key):
        if not root: return BSTNode(key)
        if key < root.key: root.left = self._insert(root.left, key)
        else: root.right = self._insert(root.right, key)
        return root

    def inorder(self, root):
        return self.inorder(root.left) + [root.key] + self.inorder(root.right) if root else []

# Hash Table with Separate Chaining
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def insert(self, key, value):
        idx = hash(key) % self.size
        for item in self.table[idx]:
            if item[0] == key:
                item[1] = value
                return
        self.table[idx].append([key, value])

    def get(self, key):
        idx = hash(key) % self.size
        for item in self.table[idx]:
            if item[0] == key: return item[1]
        return None