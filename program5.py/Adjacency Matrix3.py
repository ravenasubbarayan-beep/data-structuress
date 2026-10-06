from collections import deque

n = int(input("Enter number of vertices: "))

graph = [[] for _ in range(n)]

edges = int(input("Enter number of edges: "))

for i in range(edges):
    u, v = map(int, input("Enter edge: ").split())
    graph[u].append(v)
    graph[v].append(u)

start = int(input("Enter starting vertex: "))

def bfs(start):
    visited = [False] * n
    queue = deque([start])
    visited[start] = True

    print("BFS:", end=" ")

    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for x in graph[v]:
            if not visited[x]:
                visited[x] = True
                queue.append(x)

def dfs(v, visited):
    visited[v] = True
    print(v, end=" ")

    for x in graph[v]:
        if not visited[x]:
            dfs(x, visited)

print("\nGraph:", graph)

bfs(start)

print("\nDFS:", end=" ")
dfs(start, [False] * n)