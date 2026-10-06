# Kruskal's Algorithm

edges = [
    (1, 2, 10),
    (1, 3, 6),
    (1, 4, 5),
    (2, 4, 15),
    (3, 4, 4),
    (2, 3, 7)
]

parent = [0, 1, 2, 3, 4]

def find(i):
    while parent[i] != i:
        i = parent[i]
    return i

def union(i, j):
    a = find(i)
    b = find(j)
    parent[a] = b

edges.sort(key=lambda x: x[2])

mst = []
cost = 0

for u, v, weight in edges:
    if find(u) != find(v):
        union(u, v)
        mst.append((u, v, weight))
        cost += weight

print("Minimum Spanning Tree:")

for u, v, weight in mst:
    print(u, "-", v, ":", weight)

print("Minimum Cost =", cost)