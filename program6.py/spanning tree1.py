# Prim's Algorithm

V = 5
INF = 999

graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

selected = [False] * V
selected[0] = True

print("Edges in Minimum Spanning Tree:")

for _ in range(V - 1):
    minimum = INF
    x = y = 0

    for i in range(V):
        if selected[i]:
            for j in range(V):
                if not selected[j] and graph[i][j]:
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x = i
                        y = j

    print(chr(65 + x), "-", chr(65 + y), ":", minimum)
    selected[y] = True