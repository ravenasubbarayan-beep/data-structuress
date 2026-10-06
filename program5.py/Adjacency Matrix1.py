# Graph using Adjacency Matrix
from collections import deque

graph = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 1, 1, 0]
]

def bfs(start):
    visited = [False] * 5
    queue = deque([start])
    visited[start] = True

    print("BFS:", end=" ")
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for i in range(5):
            if graph[vertex][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)

def dfs(vertex, visited=None):
    if visited is None:
        visited = [False] * 5

    visited[vertex] = True
    print(vertex, end=" ")

    for i in range(5):
        if graph[vertex][i] == 1 and not visited[i]:
            dfs(i, visited)

print("Adjacency Matrix:")
for row in graph:
    print(row)

bfs(0)

print("\nDFS:", end=" ")
dfs(0)