# Kruskal's Algorithm

edges = [
    (10, 'A', 'B'),
    (6, 'A', 'C'),
    (5, 'B', 'C'),
    (15, 'B', 'D'),
    (4, 'C', 'D')
]

parent = {}

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    parent[find(x)] = find(y)

vertices = set()

for weight, u, v in edges:
    vertices.add(u)
    vertices.add(v)

for vertex in vertices:
    parent[vertex] = vertex

edges.sort()

mst = []
total = 0

for weight, u, v in edges:
    if find(u) != find(v):
        union(u, v)
        mst.append((u, v, weight))
        total += weight

print("Edges in Minimum Spanning Tree:")

for u, v, weight in mst:
    print(u, "-", v, ":", weight)

print("Total Cost:", total)