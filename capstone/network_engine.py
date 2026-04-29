from collections import deque

class SocialEngine:
    def __init__(self):
        self.adj_list = {}
        self.profiles = {} # Hash map for user data

    def add_user(self, name, interests):
        self.profiles[name] = interests
        if name not in self.adj_list:
            self.adj_list[name] = []

    def add_friendship(self, u, v):
        if u in self.adj_list and v in self.adj_list:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)

    def get_shortest_path(self, start, target):
        queue = deque([[start]])
        visited = {start}
        while queue:
            path = queue.popleft()
            node = path[-1]
            if node == target: return path
            for neighbor in self.adj_list.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(path + [neighbor])
        return None

    def explore_depth(self, start, depth):
        visited = set()
        def dfs(node, d):
            if d < 0 or node in visited: return set()
            visited.add(node)
            found = {node}
            for neighbor in self.adj_list.get(node, []):
                found.update(dfs(neighbor, d - 1))
            return found
        return dfs(start, depth)