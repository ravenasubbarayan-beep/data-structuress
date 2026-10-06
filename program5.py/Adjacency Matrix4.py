from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        self.graph.setdefault(u, []).append(v)
        self.graph.setdefault(v, []).append(u)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        print("BFS:", end=" ")

        while queue:
            v = queue.popleft()
            print(v, end=" ")

            for x in self.graph[v]:
                if x not in visited:
                    visited.add(x)
                    queue.append(x)

    def dfs(self, v, visited=None):
        if visited is None:
            visited = set()

        visited.add(v)
        print(v, end=" ")

        for x in self.graph[v]:
            if x not in visited:
                self.dfs(x, visited)


g = Graph()

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "E")
g.add_edge("D", "E")

print("Graph:", g.graph)

g.bfs("A")

print("\nDFS:", end=" ")
g.dfs("A")