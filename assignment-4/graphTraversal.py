class DirectedWeightedGraph:
    def __init__(self):
        self.adj = {}

    def add_node(self, node):
        if node not in self.adj: self.adj[node] = []

    def add_edge(self, u, v, weight):
        self.add_node(u)
        self.add_node(v)
        self.adj[u].append((v, weight))

    def bfs(self, start):
        visited, queue = {start}, [start]
        order = []
        while queue:
            u = queue.pop(0)
            order.append(u)
            for v, w in self.adj.get(u, []):
                if v not in visited:
                    visited.add(v); queue.append(v)
        return order

    def dfs(self, start, visited=None):
        if visited is None: visited = set()
        visited.add(start)
        print(start, end=" ")
        for v, w in self.adj.get(start, []):
            if v not in visited:
                self.dfs(v, visited)