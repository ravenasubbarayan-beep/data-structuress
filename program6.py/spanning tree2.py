# Prim's Algorithm using Edge List

graph = {
    'A': [('B', 4), ('C', 3)],
    'B': [('A', 4), ('C', 1), ('D', 2)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 2), ('C', 4)]
}

visited = set()
visited.add('A')

mst = []
total = 0

while len(visited) < len(graph):
    minimum = None

    for u in visited:
        for v, weight in graph[u]:
            if v not in visited:
                if minimum is None or weight < minimum[2]:
                    minimum = (u, v, weight)

    u, v, weight = minimum
    visited.add(v)
    mst.append((u, v, weight))
    total += weight

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge[0], "-", edge[1], ":", edge[2])

print("Total Cost:", total)