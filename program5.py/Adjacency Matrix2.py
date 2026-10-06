from collections import deque

graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 4],
    3: [1, 4],
    4: [2, 3]
}

def bfs(start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    print("BFS:", end=" ")

    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for neighbour in graph[v]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

def dfs(v, visited=None):
    if visited is None:
        visited = set()

    visited.add(v)
    print(v, end=" ")

    for neighbour in graph[v]:
        if neighbour not in visited:
            dfs(neighbour, visited)

print("Adjacency List:")
for key, value in graph.items():
    print(key, "->", value)

bfs(0)

print("\nDFS:", end=" ")
dfs(0)