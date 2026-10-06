# Prim's Algorithm with User Input

n = int(input("Enter number of vertices: "))

graph = []

print("Enter the adjacency matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

visited = [False] * n
visited[0] = True

total = 0

print("\nMinimum Spanning Tree:")

for _ in range(n - 1):
    minimum = 9999
    x = y = -1

    for i in range(n):
        if visited[i]:
            for j in range(n):
                if not visited[j] and graph[i][j] != 0:
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x = i
                        y = j

    print(x + 1, "-", y + 1, ":", minimum)
    total += minimum
    visited[y] = True

print("Total Minimum Cost:", total)